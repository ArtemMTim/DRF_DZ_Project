from django.urls import path

from users.apps import UsersConfig
from users.views import (PaymentListApiView, UserRetrieveApiView,
                         UserUpdateApiView)

app_name = UsersConfig.name

urlpatterns = [
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="user_update"),
    path("retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("payment/", PaymentListApiView.as_view(), name="payment"),
]
