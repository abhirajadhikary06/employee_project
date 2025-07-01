from rest_framework import serializers
from .models import Performance
from employees.models import Employee
from employees.serializers import EmployeeSerializer

class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)

    class Meta:
        model = Performance
        fields = ['id', 'employee', 'employee_id', 'rating', 'review_date']