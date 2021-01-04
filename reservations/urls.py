from django.urls import path
from . import views


app_name = 'reservations'
urlpatterns = [
    path('', views.reservations_list, name='list'),
    path('make/', views.make, name='make')
]
