from rest_framework import routers

from comments.views.api import IQCommentAPI

router = routers.DefaultRouter()

router.register(r'comments', IQCommentAPI)
