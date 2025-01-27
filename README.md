# Book Review API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-5.1-brightgreen)](https://www.djangoproject.com/)

A REST API for managing books, authors, and reviews with JWT authentication and OpenAPI documentation.

## Features

- Secure JWT Authentication
- Full CRUD Functionality for Books, Authors, and Reviews
- Author Profiles: Permissions for publishing and editing
- Search & Filter: Query books by title, author, or publication date
- Pagination: Configurable, defaulting to 10 items/page
- Rate Limiting: Ensures fair usage for anonymous (100/day) and authenticated users (1000/day)
- Interactive Docs: Explore the API with Swagger or ReDoc


## Tech Stack

- **Backend**: Django 5.1 + Django REST Framework
- **Database**: SQLite (Development), PostgreSQL-ready
- **Authentication**: JWT (Simple JWT)
- **Documentation**: Swagger/ReDoc

## Quick Start

```bash
# 1. Clone repo
git clone https://github.com/AAbdelrahman911/book-review-api.git
cd book-review-api

# 2. Setup environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start server
python manage.py runserver
