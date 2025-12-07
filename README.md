# Job Finder API

JobFinder API is a backend system designed to power a job searching and job posting platform.
It connects job seekers with employers by providing RESTful endpoints for authentication, job listings, job applications, and filtering/search.

This API is built using Django and Django REST Framework (DRF) and is designed to be used by a website or mobile application.

## Features

- User authentication (Job Seekers & Employers)
- Job posting and management
- Job application system
- Token-based authentication

## Setup

1. Clone the repository
```bash
git clone <your-repo-url>
cd jobfinder
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run migrations
```bash
python manage.py migrate
```

4. Start the server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login

### Jobs
- `GET /api/jobs/` - List all jobs
- `POST /api/jobs/` - Create job (requires auth)
- `GET /api/jobs/{id}/` - Get job details
- `PUT /api/jobs/{id}/` - Update job
- `DELETE /api/jobs/{id}/` - Delete job

### Applications
- `GET /api/applications/` - List applications
- `POST /api/applications/` - Apply for job (requires auth)
- `GET /api/applications/{id}/` - Get application details
- `PUT /api/applications/{id}/` - Update application
- `DELETE /api/applications/{id}/` - Delete application

## Tech Stack

- Django 5.2.8
- Django REST Framework 3.15.2
- SQLite (development)
