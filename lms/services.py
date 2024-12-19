import stripe
import config.settings as settings

stripe.api_key =  settings.STRIPE_API_KEY

def create_stripe_price(amount):
    """Создаёт цену для оплаты в Stripe."""
    return stripe.Price.create(
        currency="usd",
        unit_amount = amount * 100,
        product_data={"title": "Оплаченный урок"},
    )
def create_stripe_session(price):
    """Создаёт сессию для оплаты в Stripe."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")