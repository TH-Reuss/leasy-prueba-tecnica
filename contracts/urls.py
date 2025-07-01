from django.urls import path
from .views import ContractListView

app_name = 'contracts'

urlpatterns = [
    path('',  ContractListView.as_view(),  name='list'),
]