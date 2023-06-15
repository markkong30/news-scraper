from flask import Flask, jsonify
from flask_cors import CORS
import concurrent.futures

from utils.scrape import fetch_news
from utils.constants import news_paths

app = Flask(__name__)
CORS(app)


@app.route("/news", methods=["GET"])
def render_news():
    newslist = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for category, path in news_paths.items():
            future = executor.submit(fetch_news, path)

            try:
                data = future.result()
                newslist.append({"category": category, "data": data})
            except Exception as exc:
                print(f"Error fetching news for {category}: {exc}")

    return jsonify({"data": newslist})


if __name__ == "__main__":
    app.run()
