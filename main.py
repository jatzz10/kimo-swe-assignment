from fastapi import FastAPI

app = FastAPI()


######## GET Endpoints ########

@app.get('/')
async def root():
    return {"message": "Backend API service is running!"}


@app.get('/courses')
async def list_courses():
    '''
    TO DOs -
    - should support 3 modes of sorting:
        - Alphabetical (based on course title, ascending) 
        - date (descending) and total course rating (descending)
        
    - support optional filtering of courses based on domain
    '''
    return {"message": "List of all courses, with support for sort & filter"}


@app.get('/courses/{course_id}')
async def find_course(course_id):
    return {"message": "Get specific course overview"}


@app.get('/courses/{course_id}/chapters/{chapter_id}')
async def find_course_chapter(course_id, chapter_id):
    return {"message": "Get a course's specific chapter info"}


######## POST Endpoints ########

@app.post('/courses/{course_id}')
async def create_course(course_id):
    # add data to mongodb
    pass


@app.post('/courses/{course_id}/chapters/{chapter_id}')
async def post_course_chapter_rating(course_id, chapter_id):
    # add data to mongodb
    pass