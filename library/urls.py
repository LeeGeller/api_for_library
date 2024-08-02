from rest_framework.routers import DefaultRouter

from library.apps import LibraryConfig
from library.views import AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')

appname = LibraryConfig.name

urlpatterns = [] + router.urls
