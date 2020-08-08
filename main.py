import requests
from lxml import html

page = requests.get("https://www.faz.net")
print(page.content)