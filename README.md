# 🚗 Auto Manage Backend

This system helps manage customers, vehicles, service jobs, mechanics, and payments in an auto service center.

## Tech Stack
- Python 3.11
- Django
- Django REST Framework
- PostgreSQL

## Setup (Local)
```bash

git clone <repository_url>
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp env.template .env      # Windows: copy env.template .env
python manage.py migrate
python manage.py runserver

