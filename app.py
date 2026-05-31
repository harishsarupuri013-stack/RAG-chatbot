from flask import Flask
from flask import render_template
from flask import request

from query_engine import ask_question


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def home():

    answer = ""

    question = ""

    if request.method == "POST":

        question = request.form["question"]

        answer = ask_question(question)

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )


if __name__ == "__main__":

    app.run(debug=True)