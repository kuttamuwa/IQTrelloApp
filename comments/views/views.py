from django.shortcuts import render

from rest_framework_mongoengine import viewsets

# Create your views here.
from comments.models.models import IQComments
from comments.models.serializers import IQCommentSerializer


class IQCommentView(viewsets.ModelViewSet):
    lookup_field = '_id'
    serializer_class = IQCommentSerializer

    def get_queryset(self):
        return IQComments.objects.all()
