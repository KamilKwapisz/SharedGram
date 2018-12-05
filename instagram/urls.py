from django.contrib import admin
from django.urls import path

from instagram.app import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
