from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.signup_page, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('home/', views.weather_map, name='home'),
    # path('globe-test/', views.test, name='weather_map')
]
