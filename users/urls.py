from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.services import toggle_token
from users.views import UsersListAPIView, UserRetrieveAPIView, UserCreateAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirm-register/<str:token>/', toggle_token, name='token_activate'),
    path('users/', UsersListAPIView.as_view(), name='users_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='users_detail'),
    path('register/', UserCreateAPIView.as_view(), name='user_register')
]
