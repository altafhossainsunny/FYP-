from django.http import JsonResponse
from django.views.decorators.http import require_GET
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """
    API Root endpoint - provides information about available endpoints
    """
    api_info = {
        "message": "Welcome to SecureCrop API",
        "version": "1.0.0",
        "description": "Secure Agricultural Management System with ML and Cybersecurity",
        "endpoints": {
            "authentication": "/api/auth/",
            "soil_inputs": "/api/soil-inputs/",
            "recommendations": "/api/recommendations/",
            "feedback": "/api/feedback/",
            "admin_logs": "/api/admin/logs/",
            "weather": "/api/weather/",
            "market": "/api/market/",
            "contact": "/api/contact/",
            "notifications": "/api/notifications/",
            "admin_panel": "/admin/"
        },
        "documentation": {
            "api_docs": "Available at /api/docs/ (if configured)",
            "admin_panel": "/admin/"
        }
    }
    
    return Response(api_info)


@require_GET
def health_check(request):
    """
    Simple health check endpoint
    """
    return JsonResponse({
        "status": "healthy",
        "service": "SecureCrop API",
        "timestamp": "2025-12-30"
    })