from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def test():
    return "welcome to Flask Page!"


if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.11.5")
