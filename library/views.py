from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from library.models import Author, Book, LogService
from library.serializer import AuthorSerializer, BookSerializer, LogServiceSerializer, LogServiceSerializerList
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
    queryset = LogService.objects.all().prefetch_related('id_books_list')
    serializer_class = LogServiceSerializerList
    permission_classes = [IsAuthenticated, IsStaff, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = '__all__'
    ordering_fields = ['date_the_book_was_taken', 'date_when_the_book_was_returned', 'book_return_date', 'user']


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

    @swagger_auto_schema(
        operation_description="Create a log entry for borrowing books. The user is automatically assigned. "
                              "id_books_list is a list with books' ids."
                              "This view create a LogService for a user.",
        request_body=LogServiceSerializer,
        responses={201: LogServiceSerializer},
        examples={
            'application/json': {
                "id_books_list": [1, 2, 3],
            }
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LogServiceUpdateAPIView(UpdateAPIView):
    queryset = LogService.objects.all()
    serializer_class = LogServiceSerializer
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        operation_description="Update a log entry to return borrowed books. The user is automatically assigned."
                              "id for returned books is an id of LogService model. "
                              "id_books_list is a list with books' ids.",
        request_body=LogServiceSerializer,
        responses={200: LogServiceSerializer},
        examples={
            'application/json': {
                "id_books_list": [1, 2, 3],
            }
        }
    )
    def post(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
