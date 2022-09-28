from . import views
from django.urls import path


urlpatterns = [
    path("registrations/", views.UserRegisterAPIView.as_view(), name='register'),
    path("login/", views.LoginAPIView.as_view(), name='login'),
    path("logout/", views.LogoutAPIView.as_view(), name='logout'),
]