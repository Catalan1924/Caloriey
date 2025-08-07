# core/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calorietracker.urls')),  # Changed from calorieapp to calorietracker
]