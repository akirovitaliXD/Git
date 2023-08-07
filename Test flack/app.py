#Импорт библий
from datetime import datetime
from flask import Flask
import json
app = Flask(__name__)
#Переменные
start = datetime.now()
info_json = dict({"start-program": start})
#Каталоги сайта API

@app.route('/time') #Время перехода в каталог
def time():
    return {"time_now":datetime.now()}

@app.route('/start-program') #Время запуска программы
def start_program():
    return {"start-program":start}

start_program()

@app.route('/server') #Потом придумаю что тут
def server():
    return
#Старт сайта
app.run('0.0.0.0')





