from django.urls import path

from rest_framework.routers import DefaultRouter

from library.apps import LibraryConfig
from library.views import AuthorViewSet, BookViewSet, LogServiceListAPIView, LogServiceRetrieveAPIView

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'books', BookViewSet, basename='books')

appname = LibraryConfig.name

urlpatterns = [
                  path('logs/', LogServiceListAPIView.as_view(), name='logs'),
                  path('logs/<int:pk>/', LogServiceRetrieveAPIView.as_view(), name='logs_detail'),
              ] + router.urls
