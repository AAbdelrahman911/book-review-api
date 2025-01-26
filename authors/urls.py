from django.urls import path, include
from . import views

urlpatterns = [
    path('authors/', views.AuthorListCreateView.as_view(), name='Author-list-create'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='Author-detail'),
    path('books/', views.BookListCreateView.as_view(), name='Book-list-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='Book-detail'),
    path('register/', views.UserRegistrationView.as_view(), name='Registration'),
    path('login/', views.UserLoginView.as_view(), name='Login'),
    path('profile/', views.ProfileView.as_view(), name='user-profile'),
    path('books/<int:book_id>/reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('books/<int:book_id>/reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),

]