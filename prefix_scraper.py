import netaddr
import nmap
import requests


def get_prefixes(asn):
    prefixes_api = 'https://api.shadowserver.org/net/asn?prefix='
    url = prefixes_api + asn
    result = requests.get(url)
    prefixes = [str(i) for i in result.json()]
    summarized_prefixes = netaddr.cidr_merge(prefixes)
    prefix_strings = [str(i) for i in summarized_prefixes]
    return(prefix_strings)
