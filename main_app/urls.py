from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cakes/', views.index, name='index'),
    path('cakes/new/', views.cake_new, name='cake_new'),
    path('cakes/<int:cake_id>/delete/', views.delete_cake, name="delete_cake"),
    path('cakes/<int:cake_id>/edit/', views.update_cake, name='update_cake'),
    path('cakes/<int:cake_id>/taste/', views.taste_cake, name='tasting'),
    path('cakes/<int:cake_id>/assoc_customizations/<int:customizations_id>/', views.assoc_customizations, name='assoc_customizations'),
    path('cakes/<int:cake_id>/assoc_customizations/<int:customizations_id>/remove', views.remove_customization, name='remove_customization'),
    path('cakes/<int:cake_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cakes/<int:cake_id>/', views.detail, name='detail'),
    path('cakes/<int:cake_id>/delete_tasting/<int:tasting_id>/', views.delete_tasting, name='delete_tasting'),
    path('accounts/signup', views.signup, name='signup'),
    
]

# Steps to create a new page
# 1. Create the path in urls.py
# 2. Create a view function
# 3. Create the template for the page