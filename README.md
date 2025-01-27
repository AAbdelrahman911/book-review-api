# Book Review API 📚

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![Django 5.1](https://img.shields.io/badge/django-5.1-brightgreen.svg)](https://www.djangoproject.com/)

A REST API for managing books, authors, and reviews with JWT authentication and OpenAPI documentation.

## Features ✨

- 🔐 JWT Authentication with refresh tokens
- 📚 CRUD operations for books/reviews
- 👩💻 Author profiles with publishing permissions
- 🔍 Search & filtering capabilities
- 📄 Pagination (10 items/page)
- ⚖️ Rate limiting (100/day anonymous, 1000/day authenticated)
- 📘 Interactive API documentation

## Quick Start 🚀

### Prerequisites
- Python 3.9+
- SQLite (included with Python)

```bash
# Clone repository
git clone https://github.com/yourusername/book-review-api.git
cd book-review-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env  # Edit with your values

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
