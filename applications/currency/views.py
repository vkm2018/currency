from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from applications.currency.models import Organisations
from applications.currency.serializers import OrganisationsSerializer


# Create your views here.

class OrganisationView(ModelViewSet):
    queryset = Organisations.objects.all()
    serializer_class = OrganisationsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)