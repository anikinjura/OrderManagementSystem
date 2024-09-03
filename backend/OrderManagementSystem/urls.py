from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reference_books/', include('reference_books.urls', namespace='reference_books')),
    path('documents/', include('documents.urls', namespace='documents')),
    path('registers/', include('registers.urls', namespace='registers')),
    path('api/reference_books/', include('reference_books.api_urls', namespace='api_reference_books')),
    path('api/documents/', include('documents.api_urls', namespace='api_documents')),
    path('api/registers/', include('registers.api_urls', namespace='api_registers')),
]
