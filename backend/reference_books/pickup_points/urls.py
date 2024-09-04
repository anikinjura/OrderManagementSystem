# backend/reference_books/pickup_points/urls.py

from django.urls import path
from . import views

app_name = 'pickup_points'

urlpatterns = [
    path('', views.PickupPointListView.as_view(), name='list'),
    path('<int:pk>/', views.PickupPointDetailView.as_view(), name='detail'),
    path('create/', views.PickupPointCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.PickupPointUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PickupPointDeleteView.as_view(), name='delete'),
]
