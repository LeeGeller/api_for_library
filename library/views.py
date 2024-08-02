from datetime import timedelta

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from library.models import Author, Book
from library.serializer import AuthorSerializer, BookSerializer
from users.permissions import IsStaff


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validate_data = serializer.validated_data
        date_the_book_was_taken = validate_data.get('date_the_book_was_taken')
        validate_data['date_when_the_book_was_returned'] = date_the_book_was_taken + timedelta(days=30)