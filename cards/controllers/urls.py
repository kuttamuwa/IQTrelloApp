from django.urls import include, path

from cards.views.routers import router

urlpatterns = [
    path('api/', include(router.urls))
]
