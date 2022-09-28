from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(min_length=6, write_only=True)
    password2 = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'full_name')
        extra_kwargs = ({
            "full_name": {
                "required": True

            }
        })
    def validate_email(self, data):
        result = User.objects.filter(email=data).exists
        if not result:
            raise serializers.ValidationError('Email already exists')
        return data

    def validate(self, attrs):
        password = attrs.pop('password1')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Don't match")
        attrs['password'] = password
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.create_activation_code()
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(min_length=6, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email is None:
            raise serializers.ValidationError('Email is required')

        if password is None:
            raise serializers.ValidationError('Password is required')

        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.get(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('User not found')
        if not user.is_active:
            raise serializers.ValidationError('User not active')
        token_key, _ = Token.objects.get_or_create(user=user)

        return {
            "token": token_key
            }