from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from activities.models import Activity, Location, Booking, ClientRegistration
from authentication.models import SportrotterUser
from payments.models import Payment
from payments.urls import app_name as payments_app
from payments.views import PaymentDetail


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ('id',)


class ActivitySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    location = LocationSerializer()
    testimonials = serializers.HyperlinkedRelatedField(
        many=True, view_name='testimonial-detail', read_only=True)

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        user = self.context.get('request').user
        return Activity.objects.create(location=location, **validated_data,
                                       creator=user)

    class Meta:
        model = Activity
        fields = '__all__'
        # depth = 1


class ClientRegistrationSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=SportrotterUser.objects.all())
    payment = serializers.HyperlinkedRelatedField(
        view_name='{}:{}'.format(payments_app, PaymentDetail.view_name),
        read_only=True)

    class Meta:
        model = ClientRegistration
        fields = ('client', 'payment')


class BookingSerializer(serializers.ModelSerializer):
    registrations = ClientRegistrationSerializer(many=True)
    activity = PrimaryKeyRelatedField(queryset=Activity.objects.all())

    class Meta:
        model = Booking
        fields = ('activity', 'date', 'registrations')

    def create(self, validated_data):
        registrations = validated_data.pop('registrations')
        activity = validated_data.pop('activity')
        booking = Booking.objects.create(activity=activity,
                                         date=validated_data.pop('date'))
        for registration in registrations:
            client = registration.get('client')
            # TODO fill in with proper amount?
            ClientRegistration.objects.create(booking=booking,
                                              client=client,
                                              payment=Payment.objects.create(
                                                  amount=100))
        return booking
