# backend/reference_books/agents/api_urls.py

from django.urls import path
from . import api_views

app_name = 'api_agents'

urlpatterns = [
    path('', api_views.AgentListAPIView.as_view(), name='list'),
    path('<int:pk>/', api_views.AgentDetailAPIView.as_view(), name='detail'),
    path('create/', api_views.AgentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/update/', api_views.AgentUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', api_views.AgentDeleteAPIView.as_view(), name='delete'),
]
