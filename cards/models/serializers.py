from rest_framework import serializers

from cards.models.models import IQCards, IQCardDurumlari


class IQCardDurumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = IQCardDurumlari
        fields = '__all__'


class IQCardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = IQCards
        fields = '__all__'
