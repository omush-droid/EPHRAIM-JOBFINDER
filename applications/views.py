from rest_framework import viewsets, permissions
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'employer':
            return Application.objects.filter(job__employer=user)
        return Application.objects.filter(applicant=user)
