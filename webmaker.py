import os
import jinja2
from flask import Flask
app = Flask(__name__)

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

def render(template,**params):
    t = jinja_env.get_template(template)
    return t.render(params)

@app.route('/index')
def mainpage():
    return render('index.html')

@app.route('/index/zametka1')
def zametka1():
    title1 = 'Поход в магазин'
    params1 = ["Зайти в магазин за покупками для празднования 'старого' нового года!!!"]
    return render('typeTemplate.html', title=title1, text=params1)

@app.route('/index/zametka2')
def zametka2():
    title2 = 'Черчение'
    params2 = ['Найти принадлежности для работы с чертежами',
               'Починить циркуль',
               'Зайти в Комус (да, да, интеграция рекламы прямо в коде)']
    return render('typeTemplate.html', title=title2, text=params2)

@app.route('/index/zametka3')
def zametka():
    title3 = 'Рыбников Ю. С.'
    params3 = ['Ноль, целковый, чекушка ...']
    return render('typeTemplate.html', title=title3, text=params3)

if __name__ == '__main__':
    app.run(debug = True)