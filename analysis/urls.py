from django.urls import path
from analysis.views import dashboard_view

urlpatterns = [
    path('dashboard/<path:filename>/', dashboard_view, name='dashboard'),
]