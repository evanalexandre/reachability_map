import netaddr
import requests
import config

ASN = config.ASN


def get_prefixes(asn):
    """Returns the list of prefixes orignated from an ASN"""
    prefixes_api = 'https://api.shadowserver.org/net/asn?prefix='
    url = prefixes_api + asn
    result = requests.get(url)
    prefixes = [str(i) for i in result.json()]
    summarized_prefixes = netaddr.cidr_merge(prefixes)
    prefix_strings = [str(i) for i in summarized_prefixes]
    return(prefix_strings)


if __name__ == '__main__':
    prefixes = get_prefixes(ASN)
    print(prefixes)