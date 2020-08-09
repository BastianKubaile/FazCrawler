import os
from lxml import etree

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
        print(link_element.get("href"))
        print(link_element.get("data-is-premium"))
        temp = {}
        temp["url"] = link_element.get("href")
        temp["is_premium"] = True if link_element.get("data-is-premium") == "true" else False
        toReturn.append(temp)
        
        i += 1

    #Form of toReturn: Array of articles, each populated with:
    #url: link to article
    #is_premium: True when article is premium
    return toReturn 

def has_flag(name):
    return os.environ.get(name) == "y"