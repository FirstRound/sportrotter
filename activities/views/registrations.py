# class ActivityRegistrationList(generics.ListAPIView):
#     view_name = 'registration-list'
#     queryset = ActivityRegistration.objects.all()
#     serializer_class = ActivityRegistrationSerializer
#
#     def filter_queryset(self, queryset):
#         username = self.request.user.username
#         return queryset.filter(users__username__icontains=username)
#
#
# class ActivityRegistrationDetail(generics.ListCreateAPIView):
#     view_name = 'registration-detail'
#     queryset = ActivityRegistration.objects.all()
#     serializer_class = ActivityRegistrationSerializer
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
