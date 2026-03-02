from flask import Flask, render_template, jsonify
import random

QUOTES = [
    {"quote": "Sometimes you win, sometimes you learn", "author": "John C. Maxwell"},
    {"quote": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"quote": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"quote": "If you tell the truth, you don't have to remember anything.", "author": "Mark Twain"},
    {"quote": "The purpose of our lives is to be happy.", "author": "Dalai Lama"},
    {"quote": "In the end, we will remember not the words of our enemies, but the silence of our friends.", "author": "Martin Luther King Jr."},
    {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"quote": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"}
]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/coin")
def coin_page():
    return render_template("coin.html")


@app.route("/random")
def random_quote_page():
    return render_template("randomquote.html")


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


@app.route("/randomquote", methods=["GET"])
@app.route("/randomQuote", methods=["GET"])
def random_quote():
    quote = random.choice(QUOTES)
    return jsonify(quote)




if __name__ == "__main__":
    app.run(debug=True)