from rest_framework import serializers

from authentication.models import SportrotterUser


class SportrotterUserSerializer(serializers.ModelSerializer):
    # serializer pulls only related activities' id
    registrations = serializers.HyperlinkedRelatedField(
        many=True, view_name='registration-detail', read_only=True)

    class Meta:
        model = SportrotterUser
        # fields = '__all__'
        fields = ('first_name', 'last_name',
                  'email', 'registrations', 'avatar', 'gender')
