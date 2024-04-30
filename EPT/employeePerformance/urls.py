from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("employee/<int:pk>", views.employeeData, name = "employee"),
    path("addEmployee/<int:pk>", views.addEmployee, name = "addEmployee"),
    path("employeeDelete/<int:pk>", views.employeeDelete, name = "employeeDelete")
]
