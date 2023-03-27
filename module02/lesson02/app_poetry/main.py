from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return """
        <h1>Hello World!</h1>
        <p style="color:crimson">Group web <b>10</b></p>
        """


if __name__ == '__main__':
    app.run(host='0.0.0.0')
