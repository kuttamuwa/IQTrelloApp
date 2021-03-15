from rest_framework import routers

from cards.views.api import IQCardAPI, IQCardDurumlariAPI

router = routers.DefaultRouter()

router.register(r'cards', IQCardAPI)
router.register(r'durum', IQCardDurumlariAPI)
