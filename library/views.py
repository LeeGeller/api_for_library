from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from library.models import Author, Book
from library.serializer import AuthorSerializer, BookSerializer
from users.permissions import IsStaff


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().prefetch_related('author')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = '__all__'
    ordering_fields = ['year_of_writen', 'publication_date', 'title', 'genre', 'author__name', 'author__surname']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()
