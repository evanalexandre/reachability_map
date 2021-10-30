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


def parse_ping_sweep(result):
    nmap = result['nmap']
    start_time = result['start_time']
    source_ip = result['source_ip']
    runtime = nmap['scanstats']['elapsed']
    command = nmap['command_line']
    uphosts = nmap['scanstats']['uphosts']
    downhosts = nmap['scanstats']['downhosts']
    insert_frame = 'INSERT INTO scans (start_time, runtime, command, uphosts, downhosts, source_ip) VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'
    insert = insert_frame.format(start_time, runtime, command, uphosts, downhosts, source_ip)
    insert_row(insert)
    select_frame = 'SELECT scan_id FROM scans WHERE start_time = "{}"'
    select = select_frame.format(start_time)
    cursor = db_connect.db.cursor()
    cursor.execute(select)
    select_result = cursor.fetchone()
    scan_id = select_result[0]
    scan = result['scan']
    for ip in scan:
        status = scan[ip]['status']['state']
        reason = scan[ip]['status']['reason']
        hostname = scan[ip]['hostnames'][0]['name']
        insert_frame = 'INSERT INTO hosts (scan_id, ipv4_address, hostname, status, reason) VALUES ("{}", "{}", "{}", "{}", "{}")'
        insert = insert_frame.format(scan_id, ip, hostname, status, reason)
        insert_row(insert)


def parse_trace(result):
    lines = result.split('\r\n')
    for line in lines:
        print(line)


if __name__ == '__main__':
    result = trace.traceroute('8.8.8.8')
    parse_trace(result)
