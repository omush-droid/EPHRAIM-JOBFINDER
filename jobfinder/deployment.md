# Deployment Guide

## Production Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file with:
```
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=your-database-url
```

### 3. Database Migration
```bash
python manage.py migrate
python manage.py collectstatic
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

## New Features Implemented

### Search & Filtering
- **Search**: `/api/jobs/?search=python` - Search in title, description, location
- **Location Filter**: `/api/jobs/?location=New York`
- **Job Type Filter**: `/api/jobs/?job_type=full-time`
- **Salary Range**: `/api/jobs/?salary_min=50000&salary_max=100000`

### Pagination
- **Jobs**: 10 per page (configurable with `page_size`)
- **Applications**: 20 per page
- Use `?page=2&page_size=5` for custom pagination

### Permissions
- **Jobs**: Only employers can create/update/delete jobs
- **Applications**: Only applicant or job employer can view/modify applications

## API Examples

```bash
# Search jobs with filters
GET /api/jobs/?search=developer&location=Remote&salary_min=60000

# Get paginated results
GET /api/jobs/?page=2&page_size=5

# Filter by job type
GET /api/jobs/?job_type=contract
```