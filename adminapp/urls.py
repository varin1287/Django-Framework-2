from django.urls import path

from adminapp import views


app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admins-user-read/', views.UserListView.as_view(), name='admins_user_read'),
    path('admins-user-create/', views.UserCreateView.as_view(), name='admins_user_create'),
    path('admins-user-update/<int:pk>/', views.UserUpdateView.as_view(), name='admins_user_update'),
    path('admins-user-delete/<int:pk>/', views.UserDeleteView.as_view(), name='admins_user_delete'),
    path('admins-products-read/', views.ProductsListView.as_view(), name='admin_products_read'),
    path('admins-products-create/', views.ProductsCreateView.as_view(), name='admins_products_create'),
    path('admins-products-update/<int:pk>/', views.ProductsUpdateView.as_view(), name='admins_products_update'),
    path('admins-products-delete/<int:pk>/', views.ProductsDeleteView.as_view(), name='admins_products_delete'),
]


