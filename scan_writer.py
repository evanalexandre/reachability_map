import db_connect
import prefix_scraper
import scan_scraper


def parse_ping_sweep(result):
    print(result)


if __name__ == '__main__':
    prefixes = prefix_scraper.get_prefixes(prefix_scraper.ASN)
    for prefix in prefixes:
        result = scan_scraper.ping_sweep(prefix)


