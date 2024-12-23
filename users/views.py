from datetime import date

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer

from .services import (
    create_stripe_price,
    create_stripe_product,
    create_stripe_session,
    prepare_data,
)


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


class PaymentCreateApiView(CreateAPIView):
    """Контроллер создания оплаты. Создаёт оплату с использованием Stripe.
    В запросе принимает параметры: type_bd (тип базы данных - course/lesson), prod_id (id продукта), price (цена).
    """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        type_bd = self.request.data.get(
            "type_bd"
        )  # получаем тип базы данных из запроса
        prod_id = self.request.data.get("prod_id")  # получаем id продукта из запроса
        price = self.request.data.get("price")  # получаем цену из запроса
        product_name, payment_obj = prepare_data(
            type_bd=type_bd, prod_id=prod_id
        )  # получаем название продукта и объект для привязки в оплате
        product = create_stripe_product(product_name)  # stripe создает продукт
        unit_price = create_stripe_price(product, price)  # stripe создает цену
        session_id, payment_link = create_stripe_session(
            unit_price
        )  # stripe создаёт сессию и ссылку на оплату
        amount = unit_price["unit_amount"] / 100  # получаем цену в долларах

        # заполняем БД оплаты данными о платеже в зависимости от типа оплаченного продукта - курс либо урок
        if type_bd == "course":
            serializer.save(
                user=self.request.user,
                payment_date=date.today(),
                session_id=session_id,
                link_to_pay=payment_link,
                amount=amount,
                payment_method="безналичная оплата",
                course=payment_obj,
            )
        elif type_bd == "lesson":
            serializer.save(
                user=self.request.user,
                payment_date=date.today(),
                session_id=session_id,
                link_to_pay=payment_link,
                amount=amount,
                payment_method="безналичная оплата",
                lesson=payment_obj,
            )
