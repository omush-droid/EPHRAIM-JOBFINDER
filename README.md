# Job Finder API

A Django REST API for job posting and application management.

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
- `GET /api/jobs/` - List all jobs (with search & filters)
- `POST /api/jobs/` - Create job (employers only)
- `GET /api/jobs/{id}/` - Get job details
- `PUT /api/jobs/{id}/` - Update job (owner only)
- `DELETE /api/jobs/{id}/` - Delete job (owner only)

#### Job Search & Filters
- `GET /api/jobs/?search=keyword` - Search in title, description, location
- `GET /api/jobs/?location=City` - Filter by location
- `GET /api/jobs/?job_type=full-time` - Filter by job type
- `GET /api/jobs/?salary_min=50000&salary_max=100000` - Filter by salary range
- `GET /api/jobs/?page=2&page_size=5` - Pagination

### Applications
- `GET /api/applications/` - List applications (paginated)
- `POST /api/applications/` - Apply for job (job seekers only)
- `GET /api/applications/{id}/` - Get application details
- `PUT /api/applications/{id}/` - Update application (owner/employer only)
- `DELETE /api/applications/{id}/` - Delete application (owner/employer only)

### Social Features
- `GET /api/social/follows/` - List users you're following
- `POST /api/social/follows/follow_user/` - Follow a user
- `POST /api/social/follows/unfollow_user/` - Unfollow a user
- `GET /api/social/notifications/` - List your notifications
- `PATCH /api/social/notifications/{id}/mark_read/` - Mark notification as read

## Tech Stack

- Django 5.2.8
- Django REST Framework 3.15.2
- Django Filter 24.3
- SQLite (development)

## New Features

- **Search & Filtering**: Search jobs by keywords, filter by location, job type, and salary range
- **Pagination**: Efficient handling of large datasets with configurable page sizes
- **Role-based Permissions**: Employers can only create/modify jobs, proper access control for applications
- **Enhanced Security**: Proper permission classes ensuring data access control
- **Social Features**: Users can follow/unfollow each other with real-time notifications
- **Notification System**: Get notified when someone follows or unfollows you
