from django.urls import path
from .views import (
    CarListView, CarBrandListView, CarModelListView, 
    CarCreateView, CarBrandCreateView, CarModelCreateView, CarUpdateView, CarDeleteView,
    CarBrandUpdateView, CarBrandDeleteView, CarModelUpdateView, CarModelDeleteView
)

app_name = 'cars'

urlpatterns = [
    path('',  CarListView.as_view(),  name='list'),
    path('create/',  CarCreateView.as_view(),  name='create'),
    path('update/<uuid:pk>/',  CarUpdateView.as_view(),  name='update'),
    path('delete/<uuid:pk>/',  CarDeleteView.as_view(),  name='delete'),

    path('brands/',  CarBrandListView.as_view(),  name='brand-list'),
    path('brands/create/',  CarBrandCreateView.as_view(),  name='brand-create'),
    path('brands/update/<uuid:pk>/',  CarBrandUpdateView.as_view(),  name='brand-update'),
    path('brands/delete/<uuid:pk>/',  CarBrandDeleteView.as_view(),  name='brand-delete'),
    path('models/',  CarModelListView.as_view(),  name='model-list'),
    path('models/create/',  CarModelCreateView.as_view(),  name='model-create'),
    path('models/update/<uuid:pk>/',  CarModelUpdateView.as_view(),  name='model-update'),
    path('models/delete/<uuid:pk>/',  CarModelDeleteView.as_view(),  name='model-delete'),
]