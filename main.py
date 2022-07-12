import requests
from time import gmtime, sleep, strftime
from proxy import proxies as proxy_arr
import random
from fake_useragent import UserAgent

url_pochta = "https://www.pochtabank.ru/"
url_fin = "https://finambank.ru/"
url_bross = "https://www.uralsib.ru/"
url_expo = "https://expobank.ru/"
url_vtb = "https://www.vtb.ru/"

ua = UserAgent()

while True:
    headers = {'User-Agent': ua.random} # Fake UserAgent
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime()) # Настоящее время

    index_proxy = random.randint(0, len(proxy_arr) - 1) # Рандомный индекс прокси

    proxies = {'http': proxy_arr[index_proxy], 'https': proxy_arr[index_proxy]} # Берем рандомный прокси по индексу

    ip = requests.get('https://ip.seeip.org', proxies=proxies).text
    print('My public IP address is: {}'.format(ip)) 

    try:
        request_pochta = requests.get(url_pochta, proxies=proxies, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Почта Банк не отвечает больше 10 секунд')
        request_pochta = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        # index_proxy = random.randint(0, len(proxy_arr) - 1) # Рандомный индекс прокси
        # proxies = {'http': proxy_arr[index_proxy], 'https': proxy_arr[index_proxy]}
        # request_pochta = requests.get(url_pochta, proxies=proxies, timeout=10).status_code
        request_pochta = None
    except:
        print('Что-то пошло не так')
        request_pochta = None        

    try:
        request_fin = requests.get(url_fin, proxies=proxies, headers=headers, timeout=10).status_code    
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Финам банк не отвечает больше 10 секунд')
        request_fin = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        # index_proxy = random.randint(0, len(proxy_arr) - 1) # Рандомный индекс прокси
        # proxies = {'http': proxy_arr[index_proxy], 'https': proxy_arr[index_proxy]}
        # request_fin = requests.get(url_fin, proxies=proxies, headers=headers, timeout=10).status_code
        request_fin = None    
    except:
        print('Что-то пошло не так')
        request_fin = None        

    try:
        request_bross = requests.get(url_bross, proxies=proxies, headers=headers, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Банк России не отвечает больше 10 секунд')
        request_bross = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        # index_proxy = random.randint(0, len(proxy_arr) - 1) # Рандомный индекс прокси
        # proxies = {'http': proxy_arr[index_proxy], 'https': proxy_arr[index_proxy]}
        # request_bross = requests.get(url_bross, proxies=proxies, headers=headers, timeout=10).status_code
        request_bross = None
    except:
        print('Что-то пошло не так')
        request_bross = None        

    try:
        request_expo = requests.get(url_expo, proxies=proxies, headers=headers, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Экспо не отвечает больше 10 секунд')
        request_expo = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        # index_proxy = random.randint(0, len(proxy_arr) - 1) # Рандомный индекс прокси
        # proxies = {'http': proxy_arr[index_proxy], 'https': proxy_arr[index_proxy]}
        # request_expo = requests.get(url_expo, proxies=proxies, headers=headers, timeout=10).status_code
        request_expo = None
    except:
        print('Что-то пошло не так')
        request_expo = None        

    try:
        request_vtb = requests.get(url_vtb, proxies=proxies, headers=headers, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('ВТБ не отвечает больше 10 секунд')
        request_vtb = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        # index_proxy = random.randint(0, len(proxy_arr) - 1) # Рандомный индекс прокси
        # proxies = {'http': proxy_arr[index_proxy], 'https': proxy_arr[index_proxy]}
        # request_vtb = requests.get(url_vtb, proxies=proxies, headers=headers, timeout=10).status_code
        request_vtb = None
    except:
        print('Что-то пошло не так')
        request_vtb = None        


    if request_pochta is None or int(request_pochta) != 200:
        print(now, request_pochta, "Почта Банк")
    if request_fin is None or int(request_fin) != 200:
        print(now, request_fin, "Финам Банк")
    if request_bross is None or int(request_bross) != 200:
        print(now, request_bross, "Банк России")
    if request_expo is None or int(request_expo) != 200:
        print(now, request_expo, "Экспо банк")
    if request_vtb is None or int(request_vtb) != 200:
        print(now, request_vtb, "ВТБ банк")