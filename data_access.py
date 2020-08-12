from pymongo import MongoClient
import json

db = None

def initialize():
    global db
    f = open("./creds.json")
    mongo_config = json.load(f)["mongo"]
    client = MongoClient(mongo_config["host"], mongo_config["port"])
    db = client[mongo_config["database"]]

def check_initialize():
    if db == None:
        initialize()

def save_article(article):
    check_initialize()
    return db.articles.insert_one(article) 