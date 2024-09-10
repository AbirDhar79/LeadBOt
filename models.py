from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['leadgen_db']
posts_collection = db['posts']

def save_posts(posts):
    posts_collection.insert_many(posts)
