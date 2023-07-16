from rest_framework.permissions import BasePermission


class PostUpdatePermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().author:
            return True
        return False



