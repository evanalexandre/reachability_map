import nmap
import prefix_scraper
import time


def ping_sweep(network):
    start_time = time.strftime('%Y-%m-%d %H:%M:%S')
    scanner = nmap.PortScanner()
    arguments = '-sP'
    result = scanner.scan(hosts=network, arguments=arguments)
    print(type(result))
    result['start_time'] = start_time
    return(result)


if __name__ == '__main__':
    prefixes = prefix_scraper.get_prefixes(prefix_scraper.ASN)
    for prefix in prefixes:
        ping_sweep(prefix)