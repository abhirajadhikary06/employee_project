from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Employee, Department

class EmployeeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.department = Department.objects.create(name='TestDept')
        self.employee = Employee.objects.create(
            user=self.user,
            name='Test Employee',
            email='test@example.com',
            phone_number='1234567890',
            address='Test Address',
            date_of_joining='2023-01-01',
            department=self.department,
            role='EMPLOYEE'
        )

    def test_employee_list(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_employee_create(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'name': 'New Employee',
            'email': 'new@example.com',
            'phone_number': '0987654321',
            'address': 'New Address',
            'date_of_joining': '2023-02-01',
            'department_id': self.department.id,
            'role': 'EMPLOYEE'
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Employee.objects.count(), 2)