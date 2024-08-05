from rest_framework.routers import DefaultRouter

from library.apps import LibraryConfig
from library.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'books', BookViewSet, basename='books')

appname = LibraryConfig.name

urlpatterns = [] + router.urls
