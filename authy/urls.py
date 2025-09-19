from django.urls import path
from . import views

app_name = 'authy'


urlpatterns = [
    path('profiles/<int:id>', views.profiles, name='profiles'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]