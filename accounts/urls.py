from . import views
from django.urls import path


urlpatterns = [
    path("registrations/", views.UserRegisterAPIView.as_view()),
    path("activation_code/<str:activation_code>/", views.Index.as_view(), name='activate_account'),
    path("login/", views.LoginAPIView.as_view(), name='login'),
    path("logout/", views.LogoutAPIView.as_view(), name='logout'),
]