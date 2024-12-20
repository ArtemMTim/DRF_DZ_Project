import stripe
import config.settings as settings
from users.models import Payment

stripe.api_key = settings.STRIPE_API_KEY


#def create_stripe_product(object):
   # """Создаёт продукт в Stripe."""
    #object = Payment.objects.get(id=payment_id)
    #print(f"object: {object}")
    #print(f"object.course: {object.course}")
    #print(f"object.lesson: {object.lesson}")
    #print(f"object.amount: {object.amount}")
    #print(f"object.payment_method: {object.payment_method}")
    #print(f"object.user: {object.user}")
    #print(f"object.date: {object.payment_date}")
    #product = object.course if object.course else object.lesson
    #print(f"product {product}")
    #stripe_product = stripe.Product.create(
        #name=product.title,
    #)
    #print(f"stripe_product: {stripe_product}")
    #return stripe_product.get("id")


#def create_stripe_price(amount, product_id):
    #"""Создаёт цену для оплаты в Stripe."""
    #return stripe.Price.create(
        #currency="usd",
        #unit_amount=amount * 100,
        #product_data={"name": product_id},
    #)




#def create_stripe_product(product_name="Product_new"):
    #"""Создаем stripe продукт"""
    #stripe_product = stripe.Product.create(name=product_name)
    #return stripe_product



#def create_stripe_price(product, amount):
    #""" Создает цену в страйпе """

    #return stripe.Price.create(
        #product=product.get('id'),
        #currency="usd",
        #unit_amount=amount * 100
    #)


def create_stripe_product():
    """Создаем stripe продукт"""
    stripe_product = stripe.Product.create(name="product_name")
    return stripe_product

def create_stripe_price(product):
    """ Создает цену в страйпе """

    return stripe.Price.create(
        product=product.get('id'),
        currency="usd",
        unit_amount=123 * 100
    )

def create_stripe_session(price):
    """Создаёт сессию для оплаты в Stripe."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
