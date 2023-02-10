from binance.client import Client

"""Вы должны вставить свой API key"""
client = Client("jW8XBOfoqnDA4rV6DvT5ftFGlLrOqc0JGQrSY6FnnjidEJuc2ncZpwBFvWjR08cM")

"""Запускаем непрерывный цикл в котором будет отслеживать динамику цены"""
while True:
    """Формируется двумерный список с длиной в 1000 
    временных отрезков с интервалом в 1 минуту, 
    нам нужен последний час поэтому срезом берем нужный интервал"""
    res_list = client.get_historical_klines("XRPUSDT", Client.KLINE_INTERVAL_1MINUTE)[940:1000]
    max_price = .0
    """Записываем в переменную max_price максимальную цену за последний час"""
    for i in res_list:
        if float(i[2]) > max_price:
            max_price = float(i[2])
    hour_now = res_list[-1][4]  # Цена закрытия сейчас (точнее минуту назад)
    """Вычисляем разницу в процентном соотношении"""
    result = ((float(max_price) - float(hour_now)) / ((float(hour_now) + float(max_price)) / 2) * 100)
    if int(result) >= 1:
        print("Цена упала на 1 процент "
              "по сравнению с максимальной ценой за последний час!")
