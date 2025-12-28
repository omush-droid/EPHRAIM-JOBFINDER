from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Job
from .serializers import JobSerializer
from .permissions import IsEmployerOrReadOnly

class JobPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [IsEmployerOrReadOnly]
    pagination_class = JobPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'job_type']
    search_fields = ['title', 'description', 'location']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        salary_min = self.request.query_params.get('salary_min')
        salary_max = self.request.query_params.get('salary_max')
        
        if salary_min:
            queryset = queryset.filter(salary__gte=salary_min)
        if salary_max:
            queryset = queryset.filter(salary__lte=salary_max)
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)
