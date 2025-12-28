import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api_endpoints():
    print("=== Job Finder API Test ===")
    
    # Test 1: Register a new user
    print("\n1. Testing User Registration...")
    register_data = {
        "username": "testuser123",
        "password": "testpass123",
        "email": "test@example.com",
        "user_type": "employer"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/register/", json=register_data)
        print(f"   Status: {response.status_code}")
        if response.status_code == 201:
            token = response.json().get('token')
            print(f"   SUCCESS: User registered, token received")
        else:
            print(f"   Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("   ERROR: Server not running. Please start with: python manage.py runserver")
        return
    
    # Test 2: Login
    print("\n2. Testing Login...")
    login_data = {
        "username": "testuser123",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/login/", json=login_data)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            token = response.json().get('token')
            print(f"   SUCCESS: Login successful")
        else:
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ERROR: {e}")
        return
    
    # Test 3: Get Jobs (no auth required)
    print("\n3. Testing Job Listing...")
    try:
        response = requests.get(f"{BASE_URL}/api/jobs/")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            jobs = response.json()
            print(f"   SUCCESS: Found {jobs.get('count', 0)} jobs")
        else:
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 4: Create Job (requires auth)
    print("\n4. Testing Job Creation...")
    headers = {"Authorization": f"Token {token}"}
    job_data = {
        "title": "API Test Job",
        "description": "This is a test job created via API",
        "location": "Remote",
        "salary": 60000,
        "job_type": "full-time"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/jobs/", json=job_data, headers=headers)
        print(f"   Status: {response.status_code}")
        if response.status_code == 201:
            job = response.json()
            print(f"   SUCCESS: Job created with ID {job.get('id')}")
        else:
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 5: Search Jobs
    print("\n5. Testing Job Search...")
    try:
        response = requests.get(f"{BASE_URL}/api/jobs/?search=test")
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            jobs = response.json()
            print(f"   SUCCESS: Search returned {jobs.get('count', 0)} results")
        else:
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 6: Social Features
    print("\n6. Testing Social Features...")
    try:
        response = requests.get(f"{BASE_URL}/api/social/follows/", headers=headers)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            follows = response.json()
            print(f"   SUCCESS: Social endpoints working")
        else:
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    print("\n=== Test Complete ===")
    print("If all tests show SUCCESS, your API is working correctly!")
    print("\nTo test manually, visit: http://127.0.0.1:8000/api/jobs/")

if __name__ == "__main__":
    test_api_endpoints()