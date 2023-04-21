from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.currency.models import Organisations, Currency, Rating
from applications.currency.serializers import *


# Create your views here.

class OrganisationView(ModelViewSet):
    queryset = Organisations.objects.all()
    serializer_class = OrganisationsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        obj, _ = Rating.objects.get_or_create(org_id=pk, owner=request.user)
        print(obj)
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj.rating = request.data['rating']
        obj.save()
        return Response(request.data, status=201)

class CurrencyView(ModelViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(oragnisation=self.request.orgranisation)

    def __str__(self):
        return self.queryset






