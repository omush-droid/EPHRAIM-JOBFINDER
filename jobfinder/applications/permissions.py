from rest_framework import permissions

class IsOwnerOrEmployer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.applicant == request.user or obj.job.employer == request.user