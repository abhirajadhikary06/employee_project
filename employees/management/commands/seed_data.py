from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee
from attendance.models import Attendance
from performance.models import Performance
from django.contrib.auth.models import User
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Seeds the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']
        
        # Create departments
        dept_objects = []
        for dept_name in departments:
            dept, _ = Department.objects.get_or_create(name=dept_name)
            dept_objects.append(dept)
        
        # Create users and employees
        for _ in range(50):
            role = random.choice(['ADMIN', 'HR', 'EMPLOYEE'])
            username = fake.user_name()
            user = User.objects.create_user(
                username=username,
                password='password123',
                email=fake.email()
            )
            employee = Employee.objects.create(
                user=user,
                name=fake.name(),
                email=user.email,
                phone_number=fake.phone_number()[:15],
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(dept_objects),
                role=role
            )
            
            # Create attendance records
            for i in range(30):
                Attendance.objects.create(
                    employee=employee,
                    date=date.today() - timedelta(days=i),
                    status=random.choice(['PRESENT', 'ABSENT', 'LATE'])
                )
            
            # Create performance records
            for i in range(3):
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database with fake data'))