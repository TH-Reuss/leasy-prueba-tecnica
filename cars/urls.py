from django.urls import path
from .views import CarListView, CarBrandListView, CarModelListView, CarCreateView

app_name = 'cars'

urlpatterns = [
    path('',  CarListView.as_view(),  name='list'),
    path('create/',  CarCreateView.as_view(),  name='create'),
    path('brands/',  CarBrandListView.as_view(),  name='brand-list'),
    path('models/',  CarModelListView.as_view(),  name='model-list'),
]