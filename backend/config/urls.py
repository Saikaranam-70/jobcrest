"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.static import serve
from rest_framework_simplejwt.views import TokenRefreshView


def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "service": "JobCrest API",
        "version": "1.0.0",
        "endpoints": {
            "admin": "/admin/",
            "api_auth": "/api/auth/",
            "api_companies": "/api/companies/",
            "api_jobs": "/api/jobs/",
            "api_applications": "/api/applications/",
            "token_refresh": "/api/auth/refresh/"
        }
    })


urlpatterns = [
    path('', health_check, name='health-check'),
    path('health/', health_check, name='health-check-alias'),
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('companies.urls')),
    path('api/', include('jobs.urls')),
    path('api/', include('applications.urls')),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

# Media files serving in development and production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
