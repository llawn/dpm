from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


def start():
    app.run(port=5000, debug=True)


if __name__ == "__main__":
    start()
