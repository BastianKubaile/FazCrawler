import os
from lxml import etree, html
import requests

def extract_articles(tree):
    toReturn = []
    i = 0
    for link_element in tree.xpath("//article//a[contains(@class, 'ContentLink')]"):
        
        #There are some videos on the page, which we don't want to parse. These don't have an href attribute
        if link_element.get("href") == None:
            continue

        if has_flag("debug"):
            print("Loop Idx: %i. Should we continue?(y/n)" % i)
            if input() == "n": break


        #The first article is hard to parse, let's skip it :D
        if i == 0:
            i += 1
            continue
        
        # We need to check which kind of article we have, and then parse that into toReturn
        temp = {}
        temp["url"] = link_element.get("href")
        temp["is_premium"] = True if link_element.get("data-is-premium") == "true" else False
        toReturn.append(temp)
        
        if has_flag("print"):
            print(temp)
        i += 1

    #Form of toReturn: Array of articles, each populated with:
    #url: link to article
    #is_premium: True when article is premium
    return toReturn 

def extract_article(url):
    # Extracts the data from the article
    toReturn = {}
    tree = get_tree(url)

    toReturn["article"] = _extract_text_from_page(tree)
    for other_page_url in _get_other_pages(tree):
        page_tree = get_tree(other_page_url)
        toReturn["article"] += _extract_text_from_page(page_tree)

    #Form of to Return:
    #url: The url of the article
    #header: The Header of the article(not the headline)
    #headline: The Headline of the article(below the header)
    #authors: Array of the authors
    #updated_at: The time and date last change of this article, saved as String in the format YYYY-MM-DD HH:MM
    #description: Description of the article(below the Headline)
    #article: The text of the article, saved in a string. Each p Element shall be seperated by new Lines. After an in article headline(h3), there shall be two new lines
    #article_class: The class of the article, such as Kommentar, Fraktur. Default is Nachricht
    #resort: The resort this article was published in i.e. sport, wirtschaft, politik, ...
    if has_flag("print"):
        print(toReturn)
    return toReturn

def _get_other_pages(tree):
    to_return = []
    for link_element in tree.xpath("//li[contains(@class, ' nvg-Paginator_Item') and not (contains(@class, 'nvg-Paginator_Item-current')) and not (contains(@class, 'nvg-Paginator_Item-to-next-page'))]/a"):
        to_return.append(link_element.get("href"))
    return to_return

def _extract_text_from_page(tree):
    text = ""
    for text_element in tree.xpath("//p[contains(@class, 'atc-TextParagraph')] | //h3[contains(@class, 'atc-SubHeadline')]"):
        text += text_element.text_content()
        if text_element.tag == "h3":
            text += "\n \n"
        else:
            text += "\n"
    return text

def has_flag(name):
    return os.environ.get(name) == "y"

def get_tree(url):
    return html.fromstring(requests.get(url).content)