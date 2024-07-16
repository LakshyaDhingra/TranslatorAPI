from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home2.html")


@app.route("/api/v1/<word>")
def about(word):
    new_word = word.upper()
    return {"definition": new_word, "word": word}


if __name__ == "__main__":
    app.run(debug=True, port=5001)