from django.contrib import admin
from django.urls import path
from sensors import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name="dashboard"),
    path("get-data/", views.get_data, name="get_data"),
]
