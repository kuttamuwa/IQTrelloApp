from rest_framework import serializers

from boards.models.models import IQBoard, IQBoardDurum


class IQBoardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    olusturulma_tarihi = serializers.DateTimeField()

    class Meta:
        model = IQBoard
        fields = '__all__'


class IQBoardDurumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = IQBoardDurum
        fields = '__all__'
