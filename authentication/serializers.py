from rest_framework import serializers

from authentication.models import SportrotterUser, Professional


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        exclude = ('id',)


class SportrotterUserSerializer(serializers.ModelSerializer):
    # serializer pulls only related activities' id
    registrations = serializers.HyperlinkedRelatedField(
        many=True, view_name='registration-detail', read_only=True)
    professional = ProfessionalSerializer()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        professional_data = validated_data.pop('professional')
        professional = Professional.objects.create(**professional_data)
        user = SportrotterUser.objects.create_user(
            professional=professional,
            **validated_data)
        return user

    class Meta:
        model = SportrotterUser
        fields = ('first_name', 'last_name', 'password',
                  'email', 'registrations', 'avatar_url',
                  'gender', 'professional')
