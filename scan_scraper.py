import nmap
import prefix_scraper
import time
import urllib.request


def get_external_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return(external_ip)    


def ping_sweep(network):
    start_time = time.strftime('%Y-%m-%d %H:%M:%S')
    source_ip = get_external_ip()
    scanner = nmap.PortScanner()
    arguments = '-sP'
    result = scanner.scan(hosts=network, arguments=arguments)
    result['start_time'] = start_time
    result['source_ip'] = source_ip
    return(result)


if __name__ == '__main__':
    prefixes = prefix_scraper.get_prefixes(prefix_scraper.ASN)
    for prefix in prefixes:
        ping_sweep(prefix)
