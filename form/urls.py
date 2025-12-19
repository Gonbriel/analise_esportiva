from django.urls import path, include
from form.views import home

urlpatterns = [
    path('', home, name='home'),
]