from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.hashers import make_password

from accounts.models import Account

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=8, max_length=32, write_only=True)
#     email = serializers.EmailField(max_length=50, allow_blank=False)
#
#     class Meta:
#         model = User
#         fields = ["email", "password"]
#
#     def create(self, validated_data):
#         username = validated_data["username"]
#         email = validated_data["email"]
#         password = validated_data["password"]
#         user_obj = User(username=username, email=email)
#         user_obj.set_password(password)
#         user_obj.save()
#         return

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())])

    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email','password1', 'password2')

        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True},
        # }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password1': "password field dont match !"})

        return attrs

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password1'])
        account = Account.objects.create(user=user)

        account.save()
        user.save()

        return user
#
#
class ChangePasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('old_password', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password1': "password fields dont match !"})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct !"})

        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this user !"})

        instance.set_password(validated_data['password1'])
        instance.save()

        return instance
#
#
# class UpdateProfileSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=False)
#
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('username', 'first_name', 'last_name', 'email')
#         extra_kwargs = {
#             'username': {'required': False},
#             'first_name': {'required': False},
#             'last_name': {'required': False},
#         }
#
#     def validate_email(self, value):
#         user = self.context['request'].user
#         if get_user_model().objects.exclude(pk=user.pk).filter(email=value).exists():
#             raise serializers.ValidationError(
#                 {"email": "this email is already in use !"})
#
#         return value
#
#     def validate_username(self, value):
#         user = self.context['request'].user
#         if get_user_model().objects.exclude(pk=user.pk).filter(username=value).exists():
#             raise serializers.ValidationError(
#                 {"username": "this username is not available !"})
#
#         return value
#
#     def update(self, instance, validated_data):
#         user = self.context['request'].user
#         if user.pk != instance.pk:
#             raise serializers.ValidationError(
#                 {"authorize": "you dont have permission for this user !"})
#
#         if 'first_name' in validated_data:
#             instance.first_name = validated_data['first_name']
#         if 'last_name' in validated_data:
#             instance.last_name = validated_data['last_name']
#         if 'email' in validated_data:
#             instance.email = validated_data['email']
#         if 'username' in validated_data:
#             instance.username = validated_data['username']
#
#         instance.save()
#         return instance