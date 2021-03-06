from rest_framework import permissions
from meetings.models import User


class MaintainerPermission(permissions.IsAuthenticated):
    """Maintainer权限"""
    message = '需要Maintainer权限！！！'
    level = 2

    def has_permission(self, request, view):  # 对于列表的访问权限
        if request.user.is_anonymous:
            return False
        if not request.user.level:
            return False
        if request.user.level >= self.level:
            if User.objects.get(id=request.user.id, level=request.user.level):
                return True
            else:
                return False
        else:
            return False

    def has_object_permission(self, request, view, obj):  # 对于对象的访问权限
        return self.has_permission(request, view)


class AdminPermission(MaintainerPermission):
    """管理员权限"""
    message = '需要管理员权限！！！'
    level = 3
