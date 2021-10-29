import netaddr
import nmap
import requests
import datetime


def get_prefixes(asn):
    start = datetime.datetime.now()
    prefixes_api = 'https://api.shadowserver.org/net/asn?prefix='
    url = prefixes_api + asn
    result = requests.get(url)
    prefixes = [str(i) for i in result.json()]
    summarized_prefixes = netaddr.cidr_merge(prefixes)
    prefix_strings = [str(i) for i in summarized_prefixes]
    end = datetime.datetime.now()
    runtime = start - end
    return(prefix_strings)