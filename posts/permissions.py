from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, OPTIONS requests
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
