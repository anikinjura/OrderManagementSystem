# backend/reference_books/agents/urls.py

from django.urls import path
from . import views

app_name = 'agents'

urlpatterns = [
    path('', views.AgentListView.as_view(), name='list'),
    path('<int:pk>/', views.AgentDetailView.as_view(), name='detail'),
    path('create/', views.AgentCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.AgentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AgentDeleteView.as_view(), name='delete'),
]
