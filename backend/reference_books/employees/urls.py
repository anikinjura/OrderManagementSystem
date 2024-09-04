# backend/reference_books/employees/urls.py

from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
    path('create/', views.EmployeeCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='delete'),
]
