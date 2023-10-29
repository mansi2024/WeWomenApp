from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name=""),

    path('ImageShow', views.logout, name="logout"),

   
]