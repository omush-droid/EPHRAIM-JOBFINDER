from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        'message': 'Job Finder API',
        'version': '1.0',
        'endpoints': {
            'auth': '/api/auth/register/, /api/auth/login/',
            'jobs': '/api/jobs/',
            'applications': '/api/applications/',
            'social': '/api/social/follows/, /api/social/notifications/'
        }
    })