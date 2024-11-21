from django.urls import path
from django.contrib.auth.views import LogoutView 
from . import views
from django.urls import path

app_name = "users_app"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),  
    path('logout/', LogoutView.as_view(), name='user-logout'), 
    path('logout/success/', views.CerrarSesion.as_view(), name='logout_success'), 
    path(
        'users/register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'users/update-password/<pk>/', 
        views.UpdatePasswordView.as_view(),
        name='user-update_password',
    ),
    path(
        'users/update/<pk>/', 
        views.UserUpdateView.as_view(),
        name='user-update',
    ),
    path(
        'users/delete/<pk>/', 
        views.UserDeleteView.as_view(),
        name='user-delete',
    ),
    path(
        'users/lista/', 
        views.UserListView.as_view(),
        name='user-lista',
    ),
]