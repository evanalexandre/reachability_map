import nmap
import prefix_scraper


def ping_sweep(network):
    scanner = nmap.PortScanner()
    arguments = '-sP'
    result = scanner.scan(hosts=network, arguments=arguments)
    return(result)


if __name__ == '__main__':
    prefixes = prefix_scraper.get_prefixes(prefix_scraper.ASN)
    for prefix in prefixes:
        ping_sweep(prefix)