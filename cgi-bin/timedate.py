#!/usr/bin/env python3
import datetime

#Переменные
a = datetime.datetime.today()
#Вывод в консоль
print("Год:", a.year)
print("Месяц:", a.month)
print("День:", a.day)
print("Час:", a.hour)
print("Минут:", a.minute)
print("Секунд:", a.second)


print("Content-type: text/html")
print()
print("<h1>Время во Владивостоке</h1>")
print("Сейчас", a.year, "год,", a.month, "месяц,", a.day, "день,", a.hour,  )
