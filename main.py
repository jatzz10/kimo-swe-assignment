from fastapi import FastAPI
from pymongo import MongoClient

from routers import courses as courses_router
from config import Settings
from utilities import parse_and_load_data, create_indices

# Create FastAPI instance
app = FastAPI()

# Load app settings
settings = Settings()

# Connect to MongoDB
client = MongoClient(settings.mongo_uri)
db = client[settings.mongo_db]
collection = db[settings.mongo_db]

# Load json data to MongoDB collection
parse_and_load_data(collection)

# Create indices
create_indices(collection)

# Mount API routers
app.include_router(courses_router, prefix='/api')