from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name='home'),
    path('login/', views.register, name='register')
]
