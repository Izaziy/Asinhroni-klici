from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/coin")
def coin_page():
    return render_template("coin.html")


@app.route("/coinFlip", methods=["GET"])
def coin_flip():
    rnd = random.randint(0, 1)
    if rnd == 1:
        status = "head"
        img = "https://i.postimg.cc/CBNJNfDJ/head.png"
    else:
        status = "tails"
        img = "https://i.postimg.cc/zysdXN8w/tail.png"
    return jsonify({"img": img, "status": status})


if __name__ == "__main__":
    app.run(debug=True)