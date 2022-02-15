from rest_framework import permissions

# custom user PERMISSIONS
class AdminOrReadOnly(permissions.IsAuthenticated):
    # testing if user ADMIN or not
    
    def has_permission(self, request, view):
        # SAFE method only for 'GET' method
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    
     def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # review_user - is our variable in models
            return obj.review_user == request.user