from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cakes/', views.index, name='index'),
    path('cakes/<int:cake_id>/', views.detail, name='detail')
]