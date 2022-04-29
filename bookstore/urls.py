from django.urls import re_path
from bookstore import views

urlpatterns = [
    re_path(r'^users$', views.user_api),
    re_path(r'^users/([0-9]+)$', views.user_api),
]
