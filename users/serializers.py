from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payment, User


class UserSerializer(ModelSerializer):
    """Сериализатор пользователя."""

    payment = SerializerMethodField()

    def get_payment(self, user):
        return [
            f"{payment.payment_date} - lesson: {payment.lesson} - course: {payment.course}"
            for payment in Payment.objects.filter(user=user)
        ]

    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """Сериализатор оплаты."""

    class Meta:
        model = Payment
        fields = (
            "user",
            "payment_date",
            "course",
            "lesson",
            "amount",
            "payment_method",
            "session_id",
            "link_to_pay",
        )
