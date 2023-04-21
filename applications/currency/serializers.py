from rest_framework import serializers

from applications.currency.models import Organisations, Currency, Rating


class OrganisationsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Organisations
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):


    class Meta:
        model = Currency
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        rating_result = 0

        for rating in instance.ratings.all():
            rating_result += int(rating.rating)
        try:
            representation['rating'] = rating_result / instance.ratings.all().count()
        except ZeroDivisionError:
            pass

        return representation


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=1, max_value=5, required=True)

    class Meta:
        model = Rating
        fields = '__all__'







