from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path( "api/", include('price.api.urls')),
    path('<str:room_name>/', views.room, name='room'),
]