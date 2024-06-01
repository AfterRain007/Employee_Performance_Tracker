from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("updateEmployee/<int:pk>", views.updateEmployee, name = "updateEmployee"),
    path("addEmployee/", views.addEmployee, name = "addEmployee"),
    path("employeeDelete/<int:pk>", views.employeeDelete, name = "employeeDelete"),
    path("about/", views.about, name = "about"),
]