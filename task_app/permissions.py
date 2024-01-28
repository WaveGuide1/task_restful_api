from rest_framework import permissions


class IsTaskListCreator(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.userprofile == obj.created_by