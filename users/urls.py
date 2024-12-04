from users.views import UserUpdateApiView
from users.apps import UsersConfig
from django.urls import path

app_name = UsersConfig.name

urlpatterns = [
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="user_update"),
]
