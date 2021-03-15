from rest_framework import viewsets

from comments.models.models import IQComments
from comments.models.serializers import IQCommentSerializer


class IQCommentAPI(viewsets.ModelViewSet):
    queryset = IQComments.objects.all().order_by('-tarih')
    serializer_class = IQCommentSerializer
    permission_classes = [
        # IsAuthenticated,
        # IQCardPermissions
    ]

    def get_queryset(self):
        return super(IQCommentAPI, self).get_queryset()

    def create(self, request, *args, **kwargs):
        return super(IQCommentAPI, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(IQCommentAPI, self).destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(IQCommentAPI, self).update(request, *args, **kwargs)
