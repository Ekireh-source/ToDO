
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from django.urls import path

from .import views
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
   path('register/', views.RegisterApi.as_view(), name="register"),
   # path('login/', .as_view(), name="login"),
   path('login/', TokenObtainPairView.as_view(), name='login'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('me/', views.UserApi.as_view(), name="me"),
   path('logout/', views.LogOutApi.as_view(), name="logout"),
]