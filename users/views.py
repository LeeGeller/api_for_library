from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from config.settings import DEFAULT_FROM_EMAIL
from users.models import User
from users.serializer import UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
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
