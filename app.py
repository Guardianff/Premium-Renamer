#Thank you LazyDeveloper for helping me in this journey !

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@GUARDIANff'


if __name__ == "__main__":
    app.run()
