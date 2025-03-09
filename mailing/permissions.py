from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin


class IsOwnerMixin(UserPassesTestMixin):
    """
    Миксин для проверки, что пользователь является владельцем объекта.
    Используется для DetailView, UpdateView, DeleteView.
    """

    def test_func(self):
        obj = self.get_object()
        if hasattr(obj, "owner") and obj.owner == self.request.user:
            return True
        raise PermissionDenied("У вас нет прав для выполнения этого действия.")


class IsOwnerFilterMixin:
    """
    Миксин для фильтрации объектов по владельцу.
    Используется для ListView.
    """

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)
