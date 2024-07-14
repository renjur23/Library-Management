from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',CustomLoginView.as_view(),name='login'),
    path('register/',register,name='register'),
    path('home/', home, name='home'),
    path('books/',book,name='books'),
    path('books/<slug:category_slug>/',book,name='books_by_category'),  
    path('books/<slug:slug>/',book,name='books_detail'), 
    path('bookcategory/',bookcategory,name='bookcategory') 
]

