# kimo-swe-assignment

## Problem Statement
As a software engineer at KIMO, you are tasked with implementing a back-end API to serve courses. This API
will be responsible for handling requests from the front-end application, retrieving course information from
MongoDB, and returning the relevant data in a standardized format.

All course information is present on the file courses.json (as a list of courses). Specifically, each course
has the following structure:
name: The title of the course.
date: Creation date as a unix timestamp.
description: The description of the course.
domain: List of the course domain(s).
chapters: List of the course chapters. Each chapter has a title name and contents text.

## Deliverables
1. Script to parse course information from courses.json, create the appropriate databases and
collection(s) on a local instance of MongoDB, create the appropriate indices (for efficient retrieval)
and finally add the course data on the collection(s).

2. A containerized application of the back-end endpoints using FastAPI. Endpoints that need to be
included:
  1. Endpoint to get a list of all available courses. This endpoint needs to support 3 modes of
sorting: Alphabetical (based on course title, ascending), date (descending) and total course
rating (descending). Additionaly, this endpoint needs to support optional filtering of courses
based on domain.
  2. Endpoint to get the course overview.
  3. Endpoint to get specific chapter information.
  4. Endpoint to allow users to rate each chapter (positive/negative), while aggregating all ratings
for each course.

3. Tests for all created endpoints to validate that they are working as intended.

--- 

## Screenshots and Vidoes
<img width="1440" alt="Screenshot 2023-05-12 at 3 30 12 AM" src="https://github.com/jatzz10/kimo-swe-assignment/assets/41716010/9e3f0208-2125-4ab8-90ad-e797a59d446c">


<img width="1440" alt="Screenshot 2023-05-12 at 3 30 43 AM" src="https://github.com/jatzz10/kimo-swe-assignment/assets/41716010/3835a3f4-4636-43f5-98f2-8e0657fd90ed">


https://github.com/jatzz10/kimo-swe-assignment/assets/41716010/19566c6e-c4d5-495b-abd4-6cf0408ee601

