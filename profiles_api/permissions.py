from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Edit own profile"""

    def has_object_permission(self, request, view, obj):
        """check user to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnFeed(permissions.BasePermission):
    """Allow users to update own profile"""

    def has_object_permission(self, request, view, obj):
        """Check the user updating update"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
