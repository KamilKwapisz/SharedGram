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

    path('posts/', views.post_list, name="post-list"),
    path('posts/<str:post_uid>/comment', views.comment_create, name="comment-create"),
    path('posts/add', views.PostCreate.as_view(), name="post-create"),
    path('api/comment/add', views.rest_comment_add, name="api-comment-add"),

    path('test/', views.graphdb_test, name="test"),
    path('api/', include('rest_framework.urls'))
]
