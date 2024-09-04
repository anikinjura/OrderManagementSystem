# backend/reference_books/pickup_points/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PickupPoint

class PickupPointListView(ListView):
    model = PickupPoint
    template_name = 'pickup_points/pickup_point_list.html'

class PickupPointDetailView(DetailView):
    model = PickupPoint
    template_name = 'pickup_points/pickup_point_detail.html'

class PickupPointCreateView(CreateView):
    model = PickupPoint
    fields = '__all__'
    template_name = 'pickup_points/pickup_point_form.html'

class PickupPointUpdateView(UpdateView):
    model = PickupPoint
    fields = '__all__'
    template_name = 'pickup_points/pickup_point_form.html'

class PickupPointDeleteView(DeleteView):
    model = PickupPoint
    template_name = 'pickup_points/pickup_point_confirm_delete.html'
    success_url = '/'
