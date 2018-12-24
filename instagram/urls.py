from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from instagram.app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('posts/', views.post_list, name="post-list"),
    path('posts/add', views.PostCreateForm.as_view(), name="post-create"),

    path('test/', views.graphdb_test, name="test"),
]
