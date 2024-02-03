from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from payments.models import Payment
from payments.serializers import PaymentSerializer
from payments.services import PaymentService, get_payment


class PaymentListAPIView(ListAPIView):
    """Отображение списка платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated]


class PaymentCreateAPIView(CreateAPIView):
    """Создание платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    payment_service = PaymentService()

    def perform_create(self, serializer):
        payment_intent = self.payment_service.create_payment_intent()

        new_payment = serializer.save(
            user=self.request.user,
            session=payment_intent.id,
            payment_amount=payment_intent.amount
        )


class PaymentDetailAPIView(RetrieveAPIView):
    """Отображение одного платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class GetPaymentView(APIView):
    serializer_class = PaymentSerializer

    def get(self, request, payment_id):
        payment_intent = get_payment(payment_id)
        return Response({'status': payment_intent.status, 'body': str(payment_intent)})


class PaymentUpdateAPIView(UpdateAPIView):
    """Изменение платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentDeleteAPIView(DestroyAPIView):
    """Удаление платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
