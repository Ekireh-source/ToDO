from rest_framework import serializers
from .import services
from .models import User


class UserSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    phone_number = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    def to_internal_value(self,data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')
#
#
#     def validate(self, args):
#         pass
#
#     def create(self, validated_data):
#         pass
