from flask import Flask, url_for

app = Flask(__name__)


@app.route('/image_mars')
def promotion():
    return f'''<html lang="en">
                        <head>
                            <title>Привет, Марс!</title>
                        </head>
                        <body>
                            <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                        <div>Вот она какая, красная планета.</div>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
