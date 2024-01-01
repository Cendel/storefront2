from rest_framework import permissions


# we create a new class that extends the BasePermission class:
class IsAdminOrReadOnly(permissions.BasePermission):
    # here we override the has_permission method:
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

    # This is how we create a custom permission class.


class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    # first we define a constructor:
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        # to send a get request, the user should have the view permission.
