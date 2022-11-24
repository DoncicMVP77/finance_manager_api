from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from  .views import RegisterView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='authentication_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),

    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
