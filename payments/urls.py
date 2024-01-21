from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import (PaymentListAPIView, PaymentCreateAPIView, PaymentDetailAPIView,
                            PaymentUpdateAPIView, PaymentDeleteAPIView)

app_name = PaymentsConfig.name


urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
]
