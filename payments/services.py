import stripe

from config.settings import STRIPE_API_KEY
from payments.models import Payment


class PaymentService:
    def create_payment_intent(self):
        stripe.api_key = STRIPE_API_KEY
        payment_intent = stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            payment_method_types=["card"],
        )
        return payment_intent


def get_payment(payment_id):
    payment = Payment.objects.get(pk=payment_id)
    session = payment.session
    stripe.api_key = STRIPE_API_KEY
    payment_intent = stripe.PaymentIntent.retrieve(session)
    return payment_intent
