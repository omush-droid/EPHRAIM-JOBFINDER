# Job Finder Setup

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Delete existing database (if any):
```bash
del db.sqlite3
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser (optional):
```bash
python manage.py createsuperuser
```

5. Run server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- POST `/api/auth/register/` - Register new user
- POST `/api/auth/login/` - Login

### Jobs
- GET `/api/jobs/` - List all jobs
- POST `/api/jobs/` - Create job (employer only)
- GET `/api/jobs/{id}/` - Get job details
- PUT `/api/jobs/{id}/` - Update job
- DELETE `/api/jobs/{id}/` - Delete job

### Applications
- GET `/api/applications/` - List applications (filtered by user)
- POST `/api/applications/` - Apply for job
- GET `/api/applications/{id}/` - Get application details
- PUT `/api/applications/{id}/` - Update application
- DELETE `/api/applications/{id}/` - Delete application
