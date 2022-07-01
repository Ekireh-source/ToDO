from rest_framework import views, response, exceptions, permissions
from . import serializers as user_serializer
from .models import User
from rest_framework.response import Response
import uuid
from rest_framework import status
from rest_framework import serializers
from . import services, auth





class RegisterApi(views.APIView):

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)


        email = request.data["email"]
        phone_number = request.data["phone_number"]

        user = services.user_email_selector(email=email)
        user1 = services.user_phone_selector(phone_number=phone_number)

        if user is None:

            if user1 is None:

                serializer.is_valid(raise_exception=True)

                data = serializer.validated_data

                serializer.instance = services.create_user(user_dc=data)

                return response.Response(data=serializer.data)

            else:
                raise exceptions.AuthenticationFailed("Phone number already exists")

        else:
            raise exceptions.AuthenticationFailed("email already exists")




# class LoginApi(views.APIView):
#
#     def post(self, request):
#         email = request.data["email"]
#         password = request.data["password"]
#
#         user = services.user_email_selector(email=email)
#
#         if user is None:
#             raise exceptions.AuthenticationFailed("invalid Credentials")
#
#         if not user.check_password(raw_password=password):
#             raise exceptions.AuthenticationFailed("invalid Credentials ")
#
#         token = services.create_token(user_id=user.id)
#
#         resp = response.Response()
#
#         resp.set_cookie(key="jwt", value=token, httponly=True)
#
#         return resp


class UserApi(views.APIView):
    # this endpoint can only be used if user is authenticated

    authentication_classes = (auth.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogOutApi(views.APIView):
    authentication_classes = (auth.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")

        resp.data = {"message": "Logout success"}

        return resp