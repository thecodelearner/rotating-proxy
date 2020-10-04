import requests
from itertools import cycle
import traceback
# from get_proxies import get_proxies as getIPs

# getting proxies from the web is slow;


def scrape(url, proxies):
    """Scrapes url with rotating proxies

    Args:

        url (string): valid url scheme

        proxies (list<string>):
                values: `getIPs()` to fetch from the web; `proxy_list` to use hardcoded IPs
    """

    proxy_pool = cycle(proxies)

    for i in range(1, 11):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(
                url, proxies={"http": proxy, "https": proxy})
            print(response.json())
        except:
            # Most free proxies will often get connection errors.
            # You will have retry the entire request using another proxy to work.
            # We will just skip retries as mere paas time nahi hai itna bc
            print("oh fuck bitch - connnection error")
