from rest_framework import serializers
from .models import Attendance
from employees.models import Employee
from employees.serializers import EmployeeSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_id', 'date', 'status']