from rest_framework_simplejwt.views import TokenObtainPairView

from applications.account.views import *
from django.urls import path

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('change_password/', ChangePasswordView.as_view()),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordCompleteApiView.as_view())
    ]
