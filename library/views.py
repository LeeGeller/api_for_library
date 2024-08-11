from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from library.models import Author, Book, LogService
from library.serializer import AuthorSerializer, BookSerializer, LogServiceSerializer
from users.permissions import IsStaff


class LibrarianPermissionMixin(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()


class AuthorViewSet(LibrarianPermissionMixin, viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]


class BookViewSet(LibrarianPermissionMixin, viewsets.ModelViewSet):
    queryset = Book.objects.all().prefetch_related('author')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = '__all__'
    ordering_fields = ['year_of_writen', 'publication_date', 'title', 'genre', 'author__name', 'author__surname']


class LogServiceListAPIView(ListAPIView):
    queryset = LogService.objects.all().prefetch_related('book')
    serializer_class = LogServiceSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = '__all__'
    ordering_fields = ['date_the_book_was_taken', 'date_when_the_book_was_returned', 'book_return_date', ]


class LogServiceRetrieveAPIView(RetrieveAPIView):
    queryset = LogService.objects.all()
    serializer_class = LogServiceSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['date_the_book_was_taken', 'date_when_the_book_was_returned', 'book_return_date', ]


class LogServiceCreateAPIView(CreateAPIView):
    queryset = LogService.objects.all()
    serializer_class = LogServiceSerializer
    permission_classes = [IsAuthenticated, ]


class LogServiceUpdateAPIView(UpdateAPIView):
    queryset = LogService.objects.all()
    serializer_class = LogServiceSerializer
    permission_classes = [IsAuthenticated, ]
