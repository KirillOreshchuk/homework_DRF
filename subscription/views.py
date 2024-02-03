from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from education.permissions import IsSubscriber
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer


class SubscriptionCreateAPIView(CreateAPIView):
    """Создание подписки"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionDeleteAPIView(DestroyAPIView):
    """Удаление подписки"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsSubscriber]
