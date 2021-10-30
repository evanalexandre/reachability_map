import db_connect
import prefix_scraper
import scan_scraper
import trace


def insert_row(command):
    print(command)
    cursor = db_connect.db.cursor()
    cursor.execute(command)
    db_connect.db.commit()
    print(cursor.rowcount, "record inserted.")


def select_one(select):
    cursor = db_connect.db.cursor()
    cursor.execute(select)
    select_result = cursor.fetchone()
    return(select_result)


def insert_ip(ip):
    """Insert IP into table if it doesn't already exist. Returns IP ID"""
    # check if IP exists already
    select_frame = 'SELECT ipv4_id, ipv4_address FROM ipv4_addresses WHERE ipv4_address="{}"'
    select = select_frame.format(ip)
    select_result = select_one(select)
    # if IP doesn't exist yet, insert it and get the ID
    if select_result == None:
        insert_frame = 'INSERT INTO ipv4_addresses (ipv4_address) VALUES ("{}")'
        insert = insert_frame.format(ip)
        insert_row(insert)
        select_result = select_one(select)
        ip_id = select_result[0]
    else:
        ip_id = select_result[0]
    return(ip_id)


def parse_ping_sweep(result):
    nmap = result['nmap']
    start_time = result['start_time']
    source_ip = result['source_ip']
    source_ip_id = insert_ip(source_ip)
    runtime = nmap['scanstats']['elapsed']
    command = nmap['command_line']
    uphosts = nmap['scanstats']['uphosts']
    downhosts = nmap['scanstats']['downhosts']
    insert_frame = 'INSERT INTO scans (start_time, runtime, command, uphosts, downhosts, source_ipv4_id) VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'
    insert = insert_frame.format(start_time, runtime, command, uphosts, downhosts, source_ip_id)
    insert_row(insert)
    select_frame = 'SELECT scan_id FROM scans WHERE start_time = "{}"'
    select = select_frame.format(start_time)
    select_result = select_one(select)
    scan_id = select_result[0]
    scan = result['scan']
    for ip in scan:
        ip_id = insert_ip(ip)
        status = scan[ip]['status']['state']
        reason = scan[ip]['status']['reason']
        hostname = scan[ip]['hostnames'][0]['name']
        insert_frame = 'INSERT INTO hosts (scan_id, ipv4_id, hostname, status, reason) VALUES ("{}", "{}", "{}", "{}", "{}")'
        insert = insert_frame.format(scan_id, ip_id, hostname, status, reason)
        insert_row(insert)


def parse_trace(result):
    source_ip = scan_scraper.get_external_ip()
    source_ip_id = insert_ip(source_ip)
    lines = result.split('\n')
    for line in lines:
        print('Line: ', line)
        items = line.split()
        if len(items) > 1:
            if 'traceroute' in items:
                # parse first line
                destination = items[2]
                dest_ip = items[3].strip('(),')
                dest_ip_id = insert_ip(dest_ip)
                max_hops = items[4]
                packet_size = items[7]
                insert_frame = 'INSERT INTO traces (source_ipv4_id, destination, destination_ipv4_id, max_hops, packet_size) VALUES ("{}", "{}", "{}", "{}", "{}")'
                insert = insert_frame.format(source_ip_id, destination, dest_ip_id, max_hops, packet_size)
                insert_row(insert)
            else:
                hop_count = int(items[0])
                hop_name = items[1]
                hop_ip = items[2].strip('()')
                hop_ip_id = insert_ip(hop_ip)
                latency = float(items[3])
                print(hop_count, hop_name, hop_ip, latency)


if __name__ == '__main__':
    id = insert_ip('8.8.8.8')
    print(id)
