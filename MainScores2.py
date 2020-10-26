# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
# This will be done by using python’s flask library.
from flask import Flask, render_template


scores_file: str = "Scores.txt"

def score_server(score_results: str) -> None:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('template.html', my_string=str(score_results))
    app.run(host="0.0.0.0", port=8777, debug=True)


try:
    f2 = open(scores_file, "r")
    score_results: str = str(f2.readline())
    f2.close()
    score_server(score_results)
except Exception:
    score_results: str = "{ERROR}"
    score_server(score_results)
