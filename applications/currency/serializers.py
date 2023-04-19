from rest_framework import serializers

from applications.currency.models import Organisations


class OrganisationsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Organisations
        fields = '__all__'

