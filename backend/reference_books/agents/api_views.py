# backend/reference_books/agents/api_views.py

from rest_framework import generics
from .models import Agent
from .serializers import AgentSerializer

class AgentListAPIView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
