import config
import data_loader
import logging
import nmap
import prefix_scraper
import time
import urllib.request


logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.DEBUG,
    format=config.LOG_FORMAT
)


def get_external_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return(external_ip)


def ping_sweep(network):
    start_time = time.strftime('%Y-%m-%d %H:%M:%S')
    logging.info('Starting ping sweep on {}'.format(network))
    source_ip = get_external_ip()
    scanner = nmap.PortScanner()
    arguments = '-sP'
    result = scanner.scan(hosts=network, arguments=arguments)
    result['start_time'] = start_time
    result['source_ip'] = source_ip
    return(result)


def sweep_all_prefixes():
    prefixes = prefix_scraper.get_prefixes(prefix_scraper.ASN)
    for prefix in prefixes:
        result = ping_sweep(prefix)
        data_loader.parse_ping_sweep(result)


if __name__ == '__main__':
    sweep_all_prefixes()
