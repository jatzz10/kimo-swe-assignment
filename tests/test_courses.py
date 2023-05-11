import pytest
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_get_courses():
    response = client.get('/courses')
    assert response.status_code == 200


def test_get_course():
    response = client.get('/courses/Course 1')
    assert response.status_code == 200


def test_get_chapter():
    response = client.get('/courses/Course 1/chapters/0')
    assert response.status_code == 200


def test_rate_chapter():
    response = client.post('/courses/Course 1/chapters/0/rate', json={'rating': True})
    assert response.status_code == 200