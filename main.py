import os
import requests
from lxml import html

from utils import extract_articles, extract_article, get_tree
from data_access import save_article

os.environ["debug"] = "n"
os.environ["print"] = "y"

if __name__ == "__main__":
    tree = get_tree("https://www.faz.net")
    articles = extract_articles(tree)

    for article in articles:
        if article["is_premium"]:
            continue
        article = extract_article(article["url"])
        save_article(article)
        break