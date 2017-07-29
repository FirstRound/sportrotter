from rest_framework import serializers

from activities.models import Activity, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ('id',)


class ActivitySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
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

# class ActivityRegistrationSerializer(serializers.ModelSerializer):
#     activity = ActivitySerializer(read_only=True)
#     users = serializers.HyperlinkedRelatedField(many=True,
#                                                 view_name='user-detail',
#                                                 read_only=True)
#
#     class Meta:
#         model = ActivityRegistration
#         fields = ('users', 'activity')
