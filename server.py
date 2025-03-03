from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def default():
    return 'Миссия Колонизация Марса'


phrases = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']


@app.route('/promotion')
def promotion():
    return '</br>'.join(phrases)


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                            <title>Привет, Марс!</title>
                        </head>
                        <body>
                            <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                        <div>Вот она какая, красная планета.</div>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                                <title>Колонизация</title>
                            </head>
                            <body>
                                <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      {'<br>'.join(phrases)}
                    </div>
                            </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
