from django.urls import path
from .views import BulkUploadView

app_name = 'uploads'

urlpatterns = [
    path('bulk/',  BulkUploadView.as_view(),  name='bulk'),
]