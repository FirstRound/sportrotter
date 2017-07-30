# Create your views here.
from rest_framework import generics

from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'payment-detail'
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
