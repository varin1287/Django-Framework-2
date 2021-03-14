from django.urls import path

from authapp import views


app_name = 'authapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
]


