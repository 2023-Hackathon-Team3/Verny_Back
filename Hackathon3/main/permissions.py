from rest_framework import permissions


class ManagerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="manager").exists()


class UserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="user").exists()
