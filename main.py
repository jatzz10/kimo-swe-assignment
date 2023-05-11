from fastapi import FastAPI

from routers import courses as courses
from config import collection
from utils import parse_and_load_data, create_indices


# Create FastAPI instance
app = FastAPI()

# Load json data to MongoDB collection
parse_and_load_data()

# Create indices
create_indices()

@app.get("/")
async def root():
    return {"message": "Backend API is running..."}

# Mount API routers
app.include_router(courses.router, prefix='/api')