# backend/reference_books/agents/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Agent

class AgentListView(ListView):
    model = Agent
    template_name = 'agents/agent_list.html'

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agents/agent_detail.html'

class AgentCreateView(CreateView):
    model = Agent
    fields = '__all__'
    template_name = 'agents/agent_form.html'

class AgentUpdateView(UpdateView):
    model = Agent
    fields = '__all__'
    template_name = 'agents/agent_form.html'

class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'agents/agent_confirm_delete.html'
    success_url = '/'
