import db_connect
import prefix_scraper
import scan_scraper


def parse_ping_sweep(result):
    nmap = result['nmap']
    start_time = result['start_time']
    runtime = nmap['scanstats']['elapsed']
    command = nmap['command_line']
    uphosts = nmap['scanstats']['uphosts']
    downhosts = nmap['scanstats']['downhosts']
    print(start_time, runtime, command, uphosts, downhosts)
    cursor = db_connect.db.cursor()
    insert_frame = 'INSERT INTO scans (start_time, runtime, command, uphosts, downhosts) VALUES ("{}", "{}", "{}", "{}", "{}")'
    insert = insert_frame.format(start_time, runtime, command, uphosts, downhosts)
    print(insert)
    cursor.execute(insert)
    db_connect.db.commit()
    print(cursor.rowcount, "record inserted.")
    


if __name__ == '__main__':
    prefixes = prefix_scraper.get_prefixes(prefix_scraper.ASN)
    for prefix in prefixes:
        result = scan_scraper.ping_sweep(prefix)
        parse_ping_sweep(result)
        


