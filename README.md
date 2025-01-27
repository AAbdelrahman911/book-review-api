# Book Review API 📚

[![Django CI](https://github.com/yourusername/book-review-api/actions/workflows/django.yml/badge.svg)](https://github.com/yourusername/book-review-api/actions/workflows/django.yml)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django 5.1](https://img.shields.io/badge/django-5.1-brightgreen.svg)](https://docs.djangoproject.com/en/5.1/releases/5.1/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A robust Django REST API for managing books, authors, and reviews with JWT authentication, rate limiting, and comprehensive documentation.

## Table of Contents 📑

- [Features](#features-)
- [Tech Stack](#tech-stack-)
- [Quick Start](#quick-start-)
- [API Documentation](#api-documentation-)
- [Authentication](#authentication-)
- [Endpoints](#endpoints-)
- [Examples](#examples-)
- [Data Models](#data-models-)
- [Rate Limiting](#rate-limiting-)
- [Deployment](#deployment-)
- [Docker](#docker-)
- [Testing](#testing-)
- [Contributing](#contributing-)
- [Code of Conduct](#code-of-conduct-)
- [License](#license-)
- [Acknowledgments](#acknowledgments-)
- [Roadmap](#roadmap-)
- [FAQ](#faq-)
- [Contact](#contact-)

## Features ✨

- **JWT Authentication** 🔐
  - Access/Refresh tokens
  - Token rotation support
- **Book Management** 📖
  - CRUD operations for books
  - Genre-based filtering
  - Publication date tracking
- **Review System** ⭐
  - 10-star rating system
  - Comment threads
  - User-specific reviews
- **Author Profiles** 👩💻
  - Bio and birthdate
  - Publishing permissions
  - Profile pictures
- **Security** 🛡️
  - Environment-based config
  - Password validation
  - CSRF protection
- **API Features** 🌐
  - Pagination (10 items/page)
  - Search/filter capabilities
  - Throttling (100/1000 req/day)
  - OpenAPI 3.0 documentation

## Tech Stack 🛠️

| Component              | Technology                          |
|------------------------|-------------------------------------|
| **Framework**          | Django 5.1 + DRF 3.14               |
| **Authentication**     | JWT (Simple JWT 5.2)                |
| **Documentation**      | DRF Spectacular + Swagger/ReDoc     |
| **Database**           | SQLite (Dev), PostgreSQL (Prod)     |
| **API Testing**        | HTTPie + Postman                    |
| **Code Quality**       | Black + Flake8 + pre-commit         |
| **CI/CD**              | GitHub Actions                      |

## Quick Start 🚀

### Prerequisites

- Python 3.9+
- pip 23.0+
- SQLite3 (included with Python)

### Installation

1. **Clone repository**
```bash
git clone https://github.com/AAbdelrahman911/book-review-api.git
cd book-review-api
