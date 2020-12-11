from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('item', views.random_item, name='random_item'),
]