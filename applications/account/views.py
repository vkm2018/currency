from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from applications.account.serializers import RegisterSerializer, ChangePasswordSerializer, LoginSeriazlier, \
    ForgotPasswordCompleteSerializer, ForgotPasswordSerializer

User = get_user_model()


class RegisterApiView(APIView):


    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)
        email = data.get('email')

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            message = 'Вы успешно зарегистрировались.' \
                      f'На ваш {email} отправлено письмо с активацией'
            return Response(message, status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):

        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msq': 'Успешно'}, status=200)
        except:
            return Response({'msq': 'Неверный код!'}, status=400)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль успешно обновлен!')





class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSeriazlier

class ForgotPasswordApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля')


class ForgotPasswordCompleteApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Пароль успешно обновлен!')


class LogOutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return  Response('Вы успешно вышли')
        except:
            return Response(status=403)