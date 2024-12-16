from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserCreateApiView(CreateAPIView):
    """Контроллер создания пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDeleteApiView(DestroyAPIView):
    """Контроллер удаления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):
    """Контроллер изменения пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListApiView(ListAPIView):
    """Контроллер списка пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListApiView(ListAPIView):
    """Контроллер списка оплат."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("course", "lesson", "payment_method")
    ordering_fields = ("payment_date",)
