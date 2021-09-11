from rest_framework import serializers
from users_roles.models import Profile, Groups


class ProfileSerializer(serializers.ModelSerializer):
    # password no more then 128 symbols and no less then 5 symbols
    # password can't read from Client side
    password = serializers.CharField(max_length=128, min_length=5, write_only=True)
    # Client side cant send token at new registration
    #token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'created', 'is_admin', 'group', 'password', 'token']

    def create(self, validated_data):
        user = super(ProfileSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id', 'group_name', 'group_description']
