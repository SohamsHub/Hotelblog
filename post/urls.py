from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<int:id>', views.listing_room, name='listing_room'),
]