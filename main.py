from helpers.scrape import scrape
from helpers.proxies import proxy_list, get_proxies as getIPs


scrape('https://httpbin.org/ip', getIPs())
