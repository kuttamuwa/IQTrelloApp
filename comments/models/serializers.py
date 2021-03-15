from rest_framework import serializers

from comments.models.models import IQComments


class IQCommentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = IQComments
        fields = '__all__'
