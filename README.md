# Задание для отбора на стажировку:

## Как попытался реализовать проверку на состояние web-приложения:

Выбрал 5 банков, которые могли пропускать "условно бесплатные" прокси.

+ Подключил Fake Agent, чтобы отправлять в get-запросе рандомный User-Agent
+ Взял некоторые прокси, чтобы не выскакивала ошибка 429(много запросов с одного ip)
+ Делаю get-запрос на сервер по доменному имени web-приложения банка. Обрабатываю запросы и вывожу, если код ошибки не равен 200, или если прозошла какая-то ошибка.

## Как попытался реализовать проверку на состояние приложения на телефон:
+ Подключил к одной сети ноутбук и смартфон на базе IOS.
+ В настроках сети смартфона перенаправил трафик через ноутбук.
+ На ноутбуке скачал и установил программу Fiddler.
+ Установил на смартфон сертификат, чтобы расшифровывать весь HTTPS трафик, идущий с телефона.
+ На смартфоне открывал приложения банков и смотрел на какие сервера идут запросы.
+ Проблема - некоторые банки для аутентификации используют сервера Google и не понятно как оценивать состояние сервера, к которому обращается приложение.
