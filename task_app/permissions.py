from rest_framework import permissions


class IsTaskListCreator(permissions.BasePermission):

    """ Task list permission"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.userprofile == obj.created_by


class IsTaskEditingAllowed(permissions.BasePermission):
    """ Task permission"""

    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.userprofile.house is not None
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.userprofile.house == obj.task_list.house


class IsAttachmentEditingAllowed(permissions.BasePermission):
    """ Attachment permission"""

    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.userprofile.house is not None
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.userprofile.house == obj.task.task_list.house