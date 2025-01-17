from django.urls import path
from . import views

urlpatterns = [
    # Photo Gallery Views
    path('', views.photo_list, name='photo_list'),  # Home page with photo list
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),  # Photo detail view
    path('like/<int:photo_id>/', views.photo_like, name='photo_like'),  # Like/unlike photo

    # User Authentication Views
    path('register/', views.user_register, name='register'),  # User registration
    path('login/', views.user_login, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout

    # User Profile Views
    path('profile/', views.user_profile, name='profile'),  # User profile
    path('profile/edit/', views.profile_edit, name='profile_edit'),  # Edit user profile
]
    