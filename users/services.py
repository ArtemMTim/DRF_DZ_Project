import stripe

import config.settings as settings
from lms.models import Course, Lesson

stripe.api_key = settings.STRIPE_API_KEY


def prepare_data(prod_id, type_bd):
    """Подготовка данных для создания платежа.
    Возвращает название продукта и объект для привязки в оплате к объекту курса либо урока.
    """
    if type_bd == "course":
        payment_obj = Course.objects.get(id=prod_id)
        product_name = payment_obj.title
    elif type_bd == "lesson":
        payment_obj = Lesson.objects.get(id=prod_id)
        product_name = payment_obj.title
    else:
        raise Exception("Неверный тип базы данных")
    return product_name, payment_obj


def create_stripe_product(product_name):
    """Создаем stripe продукт"""
    stripe_product = stripe.Product.create(name="product_name")
    return stripe_product


def create_stripe_price(product, price):
    """Создает цену в страйпе"""

    return stripe.Price.create(
        product=product.get("id"), currency="usd", unit_amount=price * 100
    )


def create_stripe_session(price):
    """Создаёт сессию для оплаты в Stripe."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
