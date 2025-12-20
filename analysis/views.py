from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

def dashboard_view(request, filename):
    path = os.path.join(settings.MEDIA_ROOT, filename)
    
    return FileResponse(
        open(path, 'rb'),
        content_type='text/html'
    )
