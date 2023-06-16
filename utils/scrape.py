import requests
from bs4 import BeautifulSoup

from utils.constants import base_url


def fetch_news(path: str):
    # use requests library to get the page
    full_url = base_url + path
    response = requests.get(full_url)

    # create BeautifulSoup object
    soup = BeautifulSoup(response.content, "html.parser")

    # find all the articles
    articles = soup.find_all("article")
    newslist = []

    # loop through each article to find the title, link, and image source
    for article in articles:
        try:
            newsitem = article.find("h3", class_="lx-stream-post__header-title")

            title = newsitem.text.strip()

            link = newsitem.a["href"]
            full_link = base_url + link

            description = article.find("p", class_="qa-story-summary")
            description = description.text.strip()

            image = article.find("img", class_="qa-story-image")["src"]

            newsarticle = {
                "title": title,
                "description": description,
                "link": full_link,
                "image": image,
            }
            newslist.append(newsarticle)

        except:
            pass

    return newslist
