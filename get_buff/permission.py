from rest_framework import permissions

class IsPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only POST requests
        return request.method == 'POST'
    
class IsGetOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only GET requests
        return request.method == 'GET'
    
class NoPutDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, POST, and other safe methods
        return request.method in ('GET', 'POST', 'HEAD', 'OPTIONS')