from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.views import StandardResultsSetPagination

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee__name', 'date', 'status']

    def get_queryset(self):
        user = self.request.user
        if user.employee.role == 'EMPLOYEE':
            return Attendance.objects.filter(employee__user=user)
        return Attendance.objects.all()