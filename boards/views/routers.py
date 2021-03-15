from rest_framework import routers

from boards.views.api import IQBoardAPI, IQBoardDurumAPI

router = routers.DefaultRouter()

router.register(r'boards', IQBoardAPI)
router.register(r'boarddurum', IQBoardDurumAPI)
