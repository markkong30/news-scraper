import requests
from bs4 import BeautifulSoup
import json

# use requests library to get the page
response = requests.get("https://www.bbc.co.uk/news/world", verify=False)

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
        image = article.find("img", class_="qa-story-image")["src"]

        newsarticle = {"title": title, "link": link, "image": image}
        newslist.append(newsarticle)

    except:
        pass

# save the data to a JSON file
with open("news.json", "w") as f:
    json.dump({"data": newslist}, f)
