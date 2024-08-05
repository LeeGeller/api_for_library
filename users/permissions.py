from rest_framework import permissions
from rest_framework.permissions import AllowAny


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
