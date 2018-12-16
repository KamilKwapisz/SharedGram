from django.urls import path
from instagram.frontend import views
urlpatterns = [
    path('', views.index , name="index"),
]
