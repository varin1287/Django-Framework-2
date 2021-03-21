from django.urls import path, re_path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('register/', views.UserCreateView.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    # path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('verify/<int:user_id>/<hash>/', views.verify, name='verify'),

]
