from django.urls import path
from .views import (
    CarListView, CarBrandListView, CarModelListView, 
    CarCreateView, CarBrandCreateView, CarModelCreateView, CarUpdateView
)

app_name = 'cars'

urlpatterns = [
    path('',  CarListView.as_view(),  name='list'),
    path('create/',  CarCreateView.as_view(),  name='create'),
    path('update/<uuid:pk>/',  CarUpdateView.as_view(),  name='update'),

    path('brands/',  CarBrandListView.as_view(),  name='brand-list'),
    path('brands/create/',  CarBrandCreateView.as_view(),  name='brand-create'),
    path('models/',  CarModelListView.as_view(),  name='model-list'),
    path('models/create/',  CarModelCreateView.as_view(),  name='model-create'),
]