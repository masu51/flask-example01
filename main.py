import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    result = """<h1>Hello world</h1>
    <p> Пример запуска приложения в Heroku 123</P>
    <p> ещё одна строка текста</p>
    """
    return result


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
