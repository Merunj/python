from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<url_list>')
def proffesion(url_list):
    return render_template("index.html", url_list=url_list)

if __name__ == "__main__":
    app.run(debug=True)