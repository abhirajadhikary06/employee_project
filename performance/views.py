from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Performance
from .serializers import PerformanceSerializer
from employees.views import StandardResultsSetPagination

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee__name', 'rating', 'review_date']

    def get_queryset(self):
        user = self.request.user
        if user.employee.role == 'EMPLOYEE':
            return Performance.objects.filter(employee__user=user)
        return Performance.objects.all()