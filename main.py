import os
import requests
from lxml import html

from utils import extract_articles

os.environ["debug"] = "y"

page = requests.get("https://www.faz.net")
tree = html.fromstring(page.content)
extract_articles(tree)