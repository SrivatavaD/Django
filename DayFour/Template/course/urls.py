from django.contrib import admin
from django.urls import path
from core.views import home
from course.views import learn_django, learn_python


urlpatterns = [
    path('',home),
    path('dj/' , learn_django),
    path('py/' , learn_python),
]