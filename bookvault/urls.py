from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-collection/', views.my_collection, name='my_collection'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/add/', views.book_create, name='book_add'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
