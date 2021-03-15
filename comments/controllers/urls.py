from django.urls import include, path

from comments.views.routers import router

urlpatterns = [
    path('api/', include(router.urls))
]