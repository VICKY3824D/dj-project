from django.urls import include, path
from django.contrib import admin
from . import views

# URL Conf
urlpatterns = [
    path('hello/', views.salam),
    path('admin/', admin.site.urls)
]

