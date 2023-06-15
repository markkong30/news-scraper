from flask import Flask, jsonify
from flask_cors import CORS

from scrape import fetch_news


app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Resource Sharing


@app.route("/news", methods=["GET"])
def render_news():
    newslist = fetch_news()

    return jsonify({"data": newslist})


if __name__ == "__main__":
    app.run()
