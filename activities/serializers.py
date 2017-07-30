from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from activities.models import Activity, Location, Booking, ClientRegistration
from authentication.models import SportrotterUser
from payments.models import Payment
from payments.views import PaymentDetail


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ('id',)


class ActivitySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    location = LocationSerializer()
    testimonials = serializers.HyperlinkedRelatedField(
        many=True, view_name='tesimonial-detail', read_only=True)

    # def create(self, validated_data):
    #     super().create(validated_data)
    #     # create and set nested entities from validated_data
    #     pass
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
    # TODO can't resolve
    payment = serializers.HyperlinkedRelatedField(
        view_name=PaymentDetail.view_name, read_only=True)

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
            ClientRegistration.objects.create(booking=booking,
                                              client=client,
                                              payment=Payment.objects.create(
                                                  amount=100))
        return booking

# class ActivityRegistrationSerializer(serializers.ModelSerializer):
#     activity = ActivitySerializer(read_only=True)
#     users = serializers.HyperlinkedRelatedField(many=True,
#                                                 view_name='user-detail',
#                                                 read_only=True)
#
#     class Meta:
#         model = ActivityRegistration
#         fields = ('users', 'activity')
