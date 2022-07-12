import requests
from url_banks import url_expo, url_fin, url_pochta, url_pochta_mob, url_urlsb, url_vtb, url_vtb_mob, url_urlsb_mob

def check_connection(proxies, now, headers):
    # ip = requests.get('https://ip.seeip.org', proxies=proxies).text
    # print('My public IP address is: {}'.format(ip)) 
    
    try:
        request_pochta = requests.get(url_pochta, proxies=proxies, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Почта Банк не отвечает больше 10 секунд')
        request_pochta = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
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
        request_fin = None    
    except:
        print('Что-то пошло не так')
        request_fin = None        

    try:
        request_urlsb = requests.get(url_urlsb, proxies=proxies, headers=headers, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Банк России не отвечает больше 10 секунд')
        request_urlsb = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        request_urlsb = None
    except:
        print('Что-то пошло не так')
        request_urlsb = None        

    try:
        request_expo = requests.get(url_expo, proxies=proxies, headers=headers, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Экспо не отвечает больше 10 секунд')
        request_expo = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
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
        request_vtb = None
    except:
        print('Что-то пошло не так')
        request_vtb = None        

    try:
        request_pochta_mob = requests.get(url_pochta_mob, proxies=proxies, headers=headers, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('Почта Банк для мобильного сервера не отвечает больше 10 секунд')
        request_pochta_mob = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        request_pochta_mob = None
    except:
        print('Что-то пошло не так')
        request_pochta_mob = None        

    try:
        request_vtb_mob = requests.get(url_vtb_mob, proxies=proxies, headers=headers, timeout=10).status_code
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print('ВТБ мобайл не отвечает больше 10 секунд')
        request_vtb_mob = None
    except requests.exceptions.ProxyError:
        print('Не удалось подключиться к proxy. Переподключение')
        request_vtb_mob = None
    except:
        print('Что-то пошло не так')
        request_vtb_mob = None        

    # try:
    #     request_urlsb_mob = requests.get(url_urlsb_mob, proxies=proxies, headers=headers, timeout=10).status_code
    # except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
    #     print('ВТБ мобайл не отвечает больше 10 секунд')
    #     request_urlsb_mob = None
    # except requests.exceptions.ProxyError:
    #     print('Не удалось подключиться к proxy. Переподключение')
    #     request_urlsb_mob = None
    # except:
    #     print('Что-то пошло не так')
    #     request_urlsb_mob = None       


    if request_pochta is None or int(request_pochta) != 200:
        print(now, request_pochta, "Почта Банк")
    if request_pochta_mob is None or int(request_pochta_mob) != 200:
        print(now, request_pochta_mob, "Почта Банк для мобильного сервера")
    if request_fin is None or int(request_fin) != 200:
        print(now, request_fin, "Финам Банк")
    if request_urlsb is None or int(request_urlsb) != 200:
        print(now, request_urlsb, "Уралсиб")
    # if request_urlsb_mob is None or int(request_urlsb_mob) != 200:
    #     print(now, request_urlsb_mob, "Уралсиб для мобильного сервера") - требует авторизацию(401 ошибка)
    if request_expo is None or int(request_expo) != 200:
        print(now, request_expo, "Экспо банк")
    if request_vtb is None or int(request_vtb) != 200:
        print(now, request_vtb, "ВТБ банк")
    if request_vtb_mob is None or int(request_vtb_mob) != 200:
        print(now, request_vtb_mob, "ВТБ мобайл")