import secrets

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from users.models import User


def toggle_token(request, token):
    user = get_object_or_404(User, token=token)
    if user:
        user.is_active = True
        user.save()
    return HttpResponse(status=200)
