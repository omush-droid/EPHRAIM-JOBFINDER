from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from jobs.models import Job
from applications.models import Application
from social.models import Follow, Notification

User = get_user_model()

class Command(BaseCommand):
    help = 'Verify database structure and create test data'

    def handle(self, *args, **options):
        self.stdout.write("Checking database structure...")
        
        # Check models
        self.stdout.write(f"Users table: {User.objects.count()} records")
        self.stdout.write(f"Jobs table: {Job.objects.count()} records")
        self.stdout.write(f"Applications table: {Application.objects.count()} records")
        self.stdout.write(f"Follows table: {Follow.objects.count()} records")
        self.stdout.write(f"Notifications table: {Notification.objects.count()} records")
        
        # Create test data if empty
        if User.objects.count() == 0:
            self.stdout.write("\nCreating test data...")
            
            # Create users
            employer = User.objects.create_user(
                username='employer1',
                password='testpass123',
                email='employer@test.com',
                user_type='employer'
            )
            
            jobseeker = User.objects.create_user(
                username='jobseeker1',
                password='testpass123',
                email='jobseeker@test.com',
                user_type='jobseeker'
            )
            
            # Create jobs
            Job.objects.create(
                employer=employer,
                title='Python Developer',
                description='Looking for Python developer',
                location='Remote',
                salary=75000,
                job_type='full-time'
            )
            
            Job.objects.create(
                employer=employer,
                title='Frontend Developer',
                description='React developer needed',
                location='New York',
                salary=65000,
                job_type='contract'
            )
            
            self.stdout.write("Test data created successfully!")
            self.stdout.write("   - Users: employer1/jobseeker1 (password: testpass123)")
            self.stdout.write("   - Jobs: 2 sample jobs created")
        
        self.stdout.write("\nDatabase verification complete!")