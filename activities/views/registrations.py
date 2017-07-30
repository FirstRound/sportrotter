from rest_framework import generics

from activities.models import Booking
from activities.serializers import BookingSerializer


class CreateBooking(generics.CreateAPIView):
    view_name = 'create-booking'
    serializer_class = BookingSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'booking-detail'
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
