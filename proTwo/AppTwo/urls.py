from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.users, name='users'),
    path('userforms/', views.userform, name='userforms')
]