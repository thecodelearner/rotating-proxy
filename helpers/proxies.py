import requests
from lxml.html import fromstring


# hardcoded 20 proxies that should work
# comment this out if you fetch proxies via getIPs()
proxy_list = [
    '125.165.175.173:8080',
    '52.221.227.177:8080',
    '213.230.69.33:8080',
    '102.130.128.13:3128',
    '195.154.237.156:3838',
    '85.133.183.66:8080',
    '180.250.101.146:8080',
    '54.213.153.247:3128',
    '182.72.150.242:8080',
    '212.248.120.230:3128',
    '83.171.114.92:45822',
    '212.87.220.2:3128',
    '18.141.57.174:8080',
    '200.73.129.128:8888',
    '95.174.67.50:18080',
    '103.247.219.30:36295',
    '62.171.153.79:8888',
    '62.210.172.164:3128',
    '163.172.89.60:3838',
    '159.224.243.185:37793'
]


def get_proxies():
    """
    Fetch proxy IPs from 'https://free-proxy-list.net'

    Returns a list of Proxy IPs; most of which are doomed.

    Returns:
        list<string>
    """

    print("fetching proxies")
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                              i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
            print("ading proxy " + proxy + " to pool")
    return proxies
