import os
from pymongo import MongoClient


def connect_mongodb():
    MONGODB_USER = 'jsharmaishere' # os.environ.get('MONGODB_USER')
    MONGODB_PASSWORD = 'KCXRcwocxBBgKsWR' # os.environ.get('MONGODB_PASSWORD')
    MONGODB_HOST = 'cluster0.b4ad5xn.mongodb.net' # os.environ.get('MONGODB_HOST')

    # Connect to MongoDB
    client = MongoClient(f'mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}')
    db = client['courses']
    collection = db['courses']
    return collection


collection = connect_mongodb()