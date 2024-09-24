from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_details, name="courses_list"),
]
