from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsOwnerOrEmployer

class ApplicationPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('-applied_at')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrEmployer]
    pagination_class = ApplicationPagination
    
    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'employer':
            return Application.objects.filter(job__employer=user)
        return Application.objects.filter(applicant=user)
