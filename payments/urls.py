from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import (PaymentListAPIView, PaymentCreateAPIView, PaymentDetailAPIView,
                            PaymentUpdateAPIView, PaymentDeleteAPIView, GetPaymentView)

app_name = PaymentsConfig.name


urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment-list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('get/<str:payment_id>/', GetPaymentView.as_view(), name='payment-get'),
    path('update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
]
