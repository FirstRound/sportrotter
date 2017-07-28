from rest_framework import serializers

from activities.models import Activity, Location, \
    ActivityRegistration
from authentication.models import SportrotterUser


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ('id',)


class ActivitySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    # TODO address
    location = LocationSerializer()
    feedbacks = serializers.HyperlinkedRelatedField(
        many=True, view_name='feedback-detail', read_only=True)

    # def create(self, validated_data):
    #     super().create(validated_data)
    #     # create and set nested entities from validated_data
    #     pass

    class Meta:
        model = Activity
        # fields = '__all__'
        exclude = ('id',)
        # depth = 1


class SportrotterUserSerializer(serializers.ModelSerializer):
    # serializer pulls only related activities' id
    registrations = serializers.HyperlinkedRelatedField(
        many=True, view_name='registration-detail', read_only=True)

    class Meta:
        model = SportrotterUser
        # fields = '__all__'
        fields = ('first_name', 'last_name',
                  'email', 'registrations', 'avatar')


class ActivityRegistrationSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(read_only=True)
    users = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='user-detail',
                                                read_only=True)

    class Meta:
        model = ActivityRegistration
        fields = ('users', 'activity')
