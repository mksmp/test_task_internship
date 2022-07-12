from time import gmtime, sleep, strftime
from proxy import proxies as proxy_arr
import random
from fake_useragent import UserAgent
from check_connection import check_connection


ua = UserAgent()

while True:
    headers = {'User-Agent': ua.random} # Fake UserAgent
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime()) # Настоящее время

    index_proxy = random.randint(0, len(proxy_arr) - 1) # Рандомный индекс прокси

    proxies = {'http': proxy_arr[index_proxy], 'https': proxy_arr[index_proxy]} # Берем рандомный прокси по индексу

    check_connection(proxies, now, headers)
    