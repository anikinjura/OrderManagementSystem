# backend/reference_books/pickup_points/api_urls.py

from django.urls import path
from . import api_views

app_name = 'api_pickup_points'

urlpatterns = [
    path('', api_views.PickupPointListAPIView.as_view(), name='list'),
    path('<int:pk>/', api_views.PickupPointDetailAPIView.as_view(), name='detail'),
    path('create/', api_views.PickupPointCreateAPIView.as_view(), name='create'),
    path('<int:pk>/update/', api_views.PickupPointUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', api_views.PickupPointDeleteAPIView.as_view(), name='delete'),
]
