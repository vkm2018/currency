from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.currency.views import *

router = DefaultRouter()

router.register('cur', CurrencyView),
router.register('', OrganisationView),


urlpatterns = [
    path('', include(router.urls)),
]

