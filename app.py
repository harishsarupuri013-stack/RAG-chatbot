from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from query_engine import ask_question


app = Flask(__name__)


@app.route("/")

def home():

    return render_template("index.html")


@app.route("/ask", methods=["POST"])

def ask():

    data = request.get_json(silent=True) or {}

    question = data.get("question", "").strip()

    if not question:

        return jsonify(
            {
                "error": "Please enter a question."
            }
        ), 400

    answer = ask_question(question)

    return jsonify(
        {
            "question": question,
            "answer": answer
        }
    )


if __name__ == "__main__":

    app.run(debug=True)
