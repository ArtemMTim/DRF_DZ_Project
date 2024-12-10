from django.urls import path

from users.apps import UsersConfig
from users.views import (
    PaymentListApiView,
    UserRetrieveApiView,
    UserUpdateApiView,
    UserDeleteApiView,
    UserCreataAPIView,
    UserListApiView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDeleteApiView.as_view(), name="user_delete"),
    path("create/", UserCreateApiView.as_view(), name="user_create"),
    path("list/", UserListApiView.as_view(), name="user_list"),
    path("retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("payment/", PaymentListApiView.as_view(), name="payment"),
]
