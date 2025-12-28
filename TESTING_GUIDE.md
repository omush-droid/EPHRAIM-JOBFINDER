# 🧪 Job Finder API - Testing Checklist

## ✅ System Status
- [x] Django system check passed (no issues)
- [x] Database migrations applied
- [x] All apps properly configured
- [x] URL patterns configured correctly

## 🔧 Manual Testing Steps

### 1. Start the Server
```bash
python manage.py runserver
```
Server should start at: http://127.0.0.1:8000

### 2. Test Authentication Endpoints

**Register Employer:**
```bash
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json

{
  "username": "employer1",
  "password": "testpass123",
  "email": "employer@test.com",
  "user_type": "employer"
}
```

**Register Job Seeker:**
```bash
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json

{
  "username": "jobseeker1",
  "password": "testpass123",
  "email": "jobseeker@test.com",
  "user_type": "jobseeker"
}
```

**Login:**
```bash
POST http://127.0.0.1:8000/api/auth/login/
Content-Type: application/json

{
  "username": "employer1",
  "password": "testpass123"
}
```
*Save the token from response for authenticated requests*

### 3. Test Job Management

**Create Job (Employer only):**
```bash
POST http://127.0.0.1:8000/api/jobs/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{
  "title": "Python Developer",
  "description": "Looking for experienced Python developer",
  "location": "Remote",
  "salary": 75000,
  "job_type": "full-time"
}
```

**List All Jobs:**
```bash
GET http://127.0.0.1:8000/api/jobs/
```

**Search Jobs:**
```bash
GET http://127.0.0.1:8000/api/jobs/?search=python
GET http://127.0.0.1:8000/api/jobs/?location=Remote
GET http://127.0.0.1:8000/api/jobs/?job_type=full-time
GET http://127.0.0.1:8000/api/jobs/?salary_min=50000&salary_max=100000
```

### 4. Test Applications

**Apply for Job (Job Seeker only):**
```bash
POST http://127.0.0.1:8000/api/applications/
Authorization: Token JOBSEEKER_TOKEN_HERE
Content-Type: application/json

{
  "job": 1,
  "cover_letter": "I am very interested in this position."
}
```

**List Applications:**
```bash
GET http://127.0.0.1:8000/api/applications/
Authorization: Token YOUR_TOKEN_HERE
```

### 5. Test Social Features

**Follow a User:**
```bash
POST http://127.0.0.1:8000/api/social/follows/follow_user/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{
  "user_id": 2
}
```

**Check Notifications:**
```bash
GET http://127.0.0.1:8000/api/social/notifications/
Authorization: Token YOUR_TOKEN_HERE
```

**Mark Notification as Read:**
```bash
PATCH http://127.0.0.1:8000/api/social/notifications/1/mark_read/
Authorization: Token YOUR_TOKEN_HERE
```

### 6. Test Pagination

**Paginated Jobs:**
```bash
GET http://127.0.0.1:8000/api/jobs/?page=1&page_size=5
```

**Paginated Applications:**
```bash
GET http://127.0.0.1:8000/api/applications/?page=1&page_size=10
Authorization: Token YOUR_TOKEN_HERE
```

## 🎯 Expected Results

### ✅ What Should Work:
- [x] User registration for both employers and job seekers
- [x] Token-based authentication
- [x] Job creation (employers only)
- [x] Job search and filtering
- [x] Job applications (job seekers only)
- [x] User following functionality
- [x] Notification system
- [x] Pagination on all list endpoints
- [x] Proper permission controls

### ❌ What Should Fail (Security Tests):
- Job seekers trying to create jobs (403 Forbidden)
- Employers trying to apply for jobs (should work, but typically wouldn't)
- Accessing other users' applications without permission
- Following yourself (400 Bad Request)

## 🚀 Quick Test Commands

**Run automated test:**
```bash
python quick_test.py
```

**Check database:**
```bash
python manage.py verify_db
```

**Django admin (create superuser first):**
```bash
python manage.py createsuperuser
# Then visit: http://127.0.0.1:8000/admin/
```

## 📊 API Endpoints Summary

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/auth/register/` | No | Register user |
| POST | `/api/auth/login/` | No | Login user |
| GET | `/api/jobs/` | No | List jobs |
| POST | `/api/jobs/` | Yes (Employer) | Create job |
| GET | `/api/jobs/{id}/` | No | Job details |
| PUT | `/api/jobs/{id}/` | Yes (Owner) | Update job |
| DELETE | `/api/jobs/{id}/` | Yes (Owner) | Delete job |
| GET | `/api/applications/` | Yes | List applications |
| POST | `/api/applications/` | Yes | Apply for job |
| GET | `/api/social/follows/` | Yes | List following |
| POST | `/api/social/follows/follow_user/` | Yes | Follow user |
| POST | `/api/social/follows/unfollow_user/` | Yes | Unfollow user |
| GET | `/api/social/notifications/` | Yes | List notifications |

## 🎉 Success Criteria
- All endpoints return appropriate HTTP status codes
- Authentication works correctly
- Permissions are enforced
- Search and filtering work
- Pagination is functional
- Social features create notifications
- No server errors in console