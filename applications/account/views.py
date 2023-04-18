from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer

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
