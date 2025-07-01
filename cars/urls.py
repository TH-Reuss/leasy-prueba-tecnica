from django.urls import path
from .views import CarListView, CarBrandListView, CarModelListView

app_name = 'cars'

urlpatterns = [
    path('',  CarListView.as_view(),  name='list'),
    path('brands/',  CarBrandListView.as_view(),  name='brand-list'),
    path('models/',  CarModelListView.as_view(),  name='model-list'),
]