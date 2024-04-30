from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("updateEmployee/<int:pk>", views.updateEmployee, name = "updateEmployee"),
    path("addEmployee/<int:pk>", views.addEmployee, name = "addEmployee"),
    path("employeeDelete/<int:pk>", views.employeeDelete, name = "employeeDelete")
]
