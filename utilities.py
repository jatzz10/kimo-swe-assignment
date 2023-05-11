import json


def parse_and_load_data(collection):
    # Parse and load course data from JSON file
    with open('courses.json', 'r') as f:
        course_data = json.load(f)

    # Insert course data into MongoDB
    collection.insert_many(course_data)
    

def create_indices(collection):
    # Create indices for efficient retrieval
    collection.create_index([('name', 1)])
    collection.create_index([('date', -1)])
    collection.create_index([('domain', 1)])
