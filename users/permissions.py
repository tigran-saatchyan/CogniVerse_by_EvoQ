from rest_framework.permissions import BasePermission, SAFE_METHODS

from payments.models import Payment


class IsOwnerOrManager(BasePermission):
    """
    Custom permission to check if the user is the owner or a manager.

    This permission class is used to control access to certain actions based
    on the user's role.
    Users who are staff members (managers) are restricted from creating or
    deleting objects.

    Attributes:
        message (str): A message to be returned when permission is denied.

    Methods:
        has_permission(request, view): Check if the user has permission to
        perform the requested action.

    Usage:
        - Use this permission class to control access to create and delete
        actions based on user roles.

    Example:
        ```python
        class MyViewSet(viewsets.ModelViewSet):
            permission_classes = [IsOwnerOrManager]
            ...
        ```
    """

    message = ""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in ["POST", "DELETE"]:
                if request.user.is_staff:
                    self.message = (
                        "Managers are not allowed to create or delete."
                    )
                    return False

            if request.method in ['PUT', 'PATCH', 'DELETE']:
                obj = view.get_object()

                if obj.owner == request.user or request.user.is_staff:
                    return True
                else:
                    self.message = (
                        "You are allowed to access/edit only your own data."
                    )
                    return False
            return True
        return False


class IsPayed(BasePermission):
    """
    Custom permission to check if the user has paid for content.

    This permission class is used to restrict access to certain actions
    based on payment status.
    Users who have paid for content or are staff members (admins) have
    access to protected content.

    Attributes:
        message (str): A message to be returned when permission is denied.

    Methods:
        has_permission(request, view): Check if the user has permission to
        perform the requested action.

    Usage:
        - Use this permission class to control access to content based on
        payment status.

    Example:
        ```python
        class MyViewSet(viewsets.ModelViewSet):
            permission_classes = [IsPayed]
            ...
        ```
    """

    message = ""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method not in SAFE_METHODS:
                return False

            if request.user.is_staff:
                return True

            obj_model = view.get_object().__class__.__name__.lower()
            view_obj = view.get_object()

            payment_filter = {
                obj_model: view_obj,
                'user': request.user
            }
            item = Payment.objects.filter(
                **payment_filter
            ).first()

            if item:
                return True

        self.message = "You are allowed to access only paid content"
        return False


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to check if the user is the owner or has read-only
    access.

    This permission class is used to allow owners full access while
    providing read-only access to others.

    Methods:
        has_object_permission(request, view, obj): Check if the user has
        permission to perform the requested action.

    Usage:
        - Use this permission class to provide read-only access to objects
        for non-owners.

    Example:
        ```python
        class MyViewSet(viewsets.ModelViewSet):
            permission_classes = [IsOwnerOrReadOnly]
            ...
        ```
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
