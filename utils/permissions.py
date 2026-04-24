from rest_framework.permissions import BasePermission


class RolePermission(BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if not self.allowed_roles:
            return True
        return request.user.role in self.allowed_roles


class IsAdmin(RolePermission):
    allowed_roles = ["admin"]


class IsMechanic(RolePermission):
    allowed_roles = ["mechanic"]


class IsAdminOrMechanic(RolePermission):
    allowed_roles = ["admin", "mechanic"]
