from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from instagram.app import views

urlpatterns = [
    path('', include('instagram.frontend.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('test/', views.graphdb_test, name="test"),
]
