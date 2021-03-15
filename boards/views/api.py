from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from boards.models.models import IQBoard, IQBoardDurum
from boards.models.serializers import IQBoardSerializer, IQBoardDurumSerializer
from boards.views.permissions import IQBoardPermissions


class IQBoardAPI(viewsets.ModelViewSet):
    lookup_field = 'id'

    queryset = IQBoard.objects.all()
    serializer_class = IQBoardSerializer
    permission_classes = [
        # IsAuthenticated,
        # IQBoardPermissions
    ]

    def get_queryset(self):
        return super(IQBoardAPI, self).get_queryset()


class IQBoardDurumAPI(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = IQBoardDurum.objects.all()
    serializer_class = IQBoardDurumSerializer

    permission_classes = [
        # IsAuthenticated,
        # IQBoardPermissions
    ]
