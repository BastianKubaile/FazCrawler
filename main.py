import os
import requests
from lxml import html

from utils import extract_articles, extract_article, get_tree

os.environ["debug"] = "n"
os.environ["print"] = "y"

if __name__ == "__main__":
    tree = get_tree("https://www.faz.net")
    articles = extract_articles(tree)

    for article in articles:
        if article["is_premium"]:
            continue
        extract_article(article["url"])
        break