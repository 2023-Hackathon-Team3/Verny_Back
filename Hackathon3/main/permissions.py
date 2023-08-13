from rest_framework import permissions


class ManagerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="manager").exists()


#class UserOnly(permissions.BasePermission):
#    def has_permission(self, request, view):
#        return request.user.groups.filter(name="user").exists()

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user