from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from config.settings import DEFAULT_FROM_EMAIL
from users.models import User
from users.permissions import IsStaff
from users.serializer import UserSerializer, UserDetailSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            host = self.request.get_host()
            url = f"http://{host}/users/confirm-register/{user.token}/"

            send_mail(
                subject="Подтвердите почту",
                message=f"Перейдите по ссылке, чтобы подтвердить вашу электронную почту: {url}",
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersListAPIView(ListAPIView):
    queryset = User.objects.all().select_related('book')
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = ['email', 'book__title', 'book__date_the_book_was_taken',
                        'book__book_return_date', 'book__date_when_the_book_was_returned']
    ordering_fields = ['book__date_the_book_was_taken',
                       'book__book_return_date', 'book__date_when_the_book_was_returned', ]


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsStaff, ]
