from django.urls import path
from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionCreateAPIView, SubscriptionDeleteAPIView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('delete/<int:pk>/', SubscriptionDeleteAPIView.as_view(), name='subscription-delete'),
]
