from rest_framework.permissions import BasePermission, SAFE_METHODS

from payments.models import Payment


class IsOwnerOrManager(BasePermission):
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
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
