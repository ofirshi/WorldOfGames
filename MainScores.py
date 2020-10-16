# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
# This will be done by using python’s flask library.
from flask import Flask


scores_file: str = "Scores.txt"


def create_index_file(file_name: str) -> None:
    """

    :param file_name:
    :return:
    :rtype: object
    """
    try:
        f = open('index.html', 'w+')
        # message = """
        #             <html>
        #             <head>
        #             <title>Scores Game</title>
        #             </head>
        #             <body>
        # """
        # f.write(message)
        f2 = open(file_name, "r")
        score_html: str = str(f2.readline())
        message2 = '<h1>The score is <div id="score">' + score_html + '</div></h1>'
        f.write(str(message2))
        # message3 = """
        # </body>
        #             </html>
        # """
        # f.write(str(message3))
        f.close()
    except Exception:
        f = open('index.html', 'w+')
        # message = """
        #             <html>
        #             <head>
        #             <title>Scores Game</title>
        #             </head>
        #             <body>
        #             <body>
        #             <h1><div id="score" style="color:red">{ERROR}</div></h1>
        #             </body>
        #             </html>
        #         """
        message = '<h1><div id="score" style="color:red">{ERROR}</div></h1>'
        f.write(message)
        f.close()
    return


def score_server(html_file: str) -> None:
    """

    :param html_file:
    :return:
    :rtype: object
    """
    app = Flask(__name__)
    f = open(html_file, "r")
    score_html: str = str(f.readlines())
    f.close()

    @app.route('/')
    def index():
        return score_html

    app.run(host="0.0.0.0", port=8777, debug=True)


if __name__ == '__main__':
    create_index_file(scores_file)
    score_server('index.html')
