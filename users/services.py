from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from users.models import User


def toggle_token(request, token):
    user = get_object_or_404(User, token=token)
    if user:
        user.is_active = True
        user.save()
    return HttpResponse(status=200)


def check_select_related():
    users_books = User.objects.all()
    print(users_books)
    if users_books is not None:
        return users_books
    else:
        return User.objects.all()
