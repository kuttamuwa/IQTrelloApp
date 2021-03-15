from django.urls import include, path

from boards.views.routers import router

urlpatterns = [
    path('api/', include(router.urls))
]
