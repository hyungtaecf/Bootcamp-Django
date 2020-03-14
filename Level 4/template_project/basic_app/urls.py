from django.contrib import admin
from django.urls import path, include
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative_url_templates, name = 'relative'),
    path('other/',views.other,name='other'),
]
