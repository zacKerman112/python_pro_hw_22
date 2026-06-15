from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):

    def has_object_permission(self, request, view, obj) -> bool:
        if request.user and request.user.is_authenticated:
            return request.user.username == obj.username
        return False