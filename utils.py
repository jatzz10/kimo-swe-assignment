import json
from config import collection


def parse_and_load_data():
    # Parse and load course data from JSON file
    with open('courses.json', 'r') as f:
        course_data = json.load(f)

    # Add rating key in courses and chapters objects
    for course in course_data:
        course['rating'] = 0

        for chapter in course['chapters']:
            chapter['rating'] = 0
    
    # Insert course data into MongoDB
    collection.insert_many(course_data)


def create_indices():
    # Create indices for efficient retrieval
    collection.create_index([('name', 1)])
    collection.create_index([('date', -1)])
    collection.create_index([('domain', 1)])
