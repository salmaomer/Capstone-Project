from django.urls import path
from . import views

urlpatterns = [
    # CRUD Books
    path('', views.home_view, name='home'),
    path('my-collection/', views.my_collection_view, name='my_collection'),
    path('book/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('book/add/', views.book_create_view, name='book_add'),
    path('book/<int:pk>/edit/', views.book_update_view, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete_view, name='book_delete'),
    path('comment/<int:pk>/edit/', views.comment_update_view, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete_view, name='comment_delete'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
