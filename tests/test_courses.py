import pytest
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_courses_sorted_alphabetical():
    response = client.get('/api/courses?sort_by=alphabetical')
    assert response.status_code == 200

    courses = response.json()
    print(courses)
    assert len(courses) == 3

    assert courses[0]['name'] == 'Course 1'
    assert courses[1]['name'] == 'Course 2'
    assert courses[2]['name'] == 'Course 3'


def test_get_courses_sorted_date():
    response = client.get('/api/courses?sort_by=date')
    assert response.status_code == 200

    courses = response.json()['courses']
    assert len(courses) == 3

    assert courses[0]['name'] == 'Course 3'
    assert courses[1]['name'] == 'Course 2'
    assert courses[2]['name'] == 'Course 1'


def test_get_courses_sorted_rating():
    response = client.get('//apicourses?sort_by=rating')
    assert response.status_code == 200

    courses = response.json()['courses']
    assert len(courses) == 3

    assert courses[0]['name'] == 'Course 3'
    assert courses[1]['name'] == 'Course 1'
    assert courses[2]['name'] == 'Course 2'


def test_get_courses_filtered_by_domain():
    response = client.get('/api/courses?domain=Technology')
    assert response.status_code == 200

    courses = response.json()['courses']
    assert len(courses) == 2

    assert courses[0]['name'] == 'Course 1'
    assert courses[1]['name'] == 'Course 3'


def test_get_course():
    response = client.get('/api/courses/Course 1')
    assert response.status_code == 200

    course = response.json()['course']
    assert course['name'] == 'Course 1'
    # assert len(course['chapters']) == 3


def test_get_chapter():
    response = client.get('/api/courses/Course 1/chapters/0')
    assert response.status_code == 200

    chapter = response.json()['chapter']
    assert chapter['title'] == 'Chapter 1'
    assert chapter['contents'] == 'This is chapter 1.'


def test_rate_chapter_positive():
    response = client.post('/api/courses/Course 1/chapters/0/rate', json={'rating': True})
    assert response.status_code == 200

    course = client.get('/courses/course 1').json()['course']
    chapter = course['chapters'][0]
    assert chapter['rating'] == 1


def test_rate_chapter_negative():
    response = client.post('/api/courses/Course 1/chapters/0/rate', json={'rating': False})
    assert response.status_code == 200

    course = client.get('/courses/course 1').json()['course']
    chapter = course['chapters'][0]
    assert chapter['rating'] == -1