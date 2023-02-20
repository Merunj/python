﻿from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template("index.html", title="Загатовка")

if __name__ == "__main__":
    app.run(debug=True)