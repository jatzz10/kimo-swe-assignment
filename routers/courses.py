from fastapi import APIRouter, Query
from pymongo import ASCENDING, DESCENDING
from typing import List
from bson import ObjectId

from models.courses import Course, Chapter
from config import collection

router = APIRouter()


@router.get('/courses', response_model=List[Course])
def get_courses(sort_by: str = 'alphabetical', domain: List[str] = Query(None)):
    sort_dict = {
        'alphabetical': ('name', ASCENDING),
        'date': ('date', DESCENDING),
        'rating': ('rating', DESCENDING)
    }
    sort_key, sort_order = sort_dict.get(sort_by, sort_dict['alphabetical'])

    query = {}
    if domain:
        query['domain'] = {'$in': domain}

    courses = list(collection.find(query).sort(sort_key, sort_order))
    return courses


@router.get('/courses/{course_id}', response_model=Course)
def get_course(course_id: str):
    course = collection.find_one({'_id': ObjectId(course_id)})
    if course:
        return course
    else:
        return {'error': 'Course not found.'}


@router.get('/courses/{course_id}/chapters/{chapter_index}', response_model=Chapter)
def get_chapter(course_id: str, chapter_index: int):
    course = collection.find_one({'_id': ObjectId(course_id)})
    if course and chapter_index < len(course['chapters']):
        return course['chapters'][chapter_index]
    else:
        return {'error': 'Chapter not found.'}


@router.post('/courses/{course_id}/chapters/{chapter_index}/rate', response_model=Chapter)
def rate_chapter(course_id: str, chapter_index: int, rating: bool):
    course = collection.find_one({'_id': ObjectId(course_id)})
    if course and chapter_index < len(course['chapters']):
        chapters = course['chapters']
        chapters[chapter_index]['rating'] += 1 if rating else -1    
        course_rating_aggregate = sum([chapter['rating'] for chapter in chapters])
        
        collection.update_one({'_id': ObjectId(course_id)}, {'$set': {
            'chapters': chapters,
            'rating': course_rating_aggregate
        }})
        return course['chapters'][chapter_index]
    else:
        return {'error': 'Chapter not found.'}
       