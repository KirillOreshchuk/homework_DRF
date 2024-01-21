from rest_framework import serializers

from payments.models import Payment
from users.models import User


class PaymentsUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('payment_date', 'payment_amount', 'payment_method')


class UserSerializer(serializers.ModelSerializer):
    user_payments = PaymentsUserSerializer(many=True, read_only=True, source='payments')

    class Meta:
        model = User
        fields = ('email', 'password', 'user_payments',)
