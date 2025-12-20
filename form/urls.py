from django.urls import path
from form.views import home

urlpatterns = [
    path('', home, name='home'),
]