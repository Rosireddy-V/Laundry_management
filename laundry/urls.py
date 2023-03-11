from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='laundry-home'),
    path('about/', views.about, name='laundry-about'),
    path('register/',user_views.register, name='register'),
]