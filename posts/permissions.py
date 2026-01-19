from rest_framework.permissions import BasePermission,SAFE_METHODS

class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    


class AuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        owner = getattr(obj, "author", None) or getattr(obj, "owner", None) or getattr(obj, "user", None)

        if owner is None:
            return True
        
        return request.user == owner
    
