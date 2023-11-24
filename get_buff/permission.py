from rest_framework import permissions

class IsPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only POST requests
        return request.method == 'POST'