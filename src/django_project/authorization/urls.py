from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_view, name="user"),
    path('sign-in/', views.authorize_u_view),
    path('sign-up/', views.create_u_view),
]