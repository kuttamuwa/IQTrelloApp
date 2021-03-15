from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from boards.models.models import IQBoard
from cards.models.models import IQCards, IQCardDurumlari
from cards.models.serializers import IQCardSerializer, IQCardDurumSerializer
from cards.views.permissions import IQCardPermissions
from djongo import models


class IQCardAPI(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = IQCards.objects.all().order_by('-durum')
    serializer_class = IQCardSerializer
    permission_classes = [
        # IsAuthenticated,
        # IQCardPermissions
    ]

    def get_queryset(self):
        return super(IQCardAPI, self).get_queryset()


class IQCardDurumlariAPI(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = IQCardDurumlari.objects.all()
    serializer_class = IQCardDurumSerializer

    permission_classes = [
        # IsAuthenticated,
        # IQCardPermissions
    ]

    def get_queryset(self):
        return super(IQCardDurumlariAPI, self).get_queryset()
