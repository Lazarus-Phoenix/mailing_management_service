from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class IsOwnerMixin(UserPassesTestMixin):
    """
    Миксин для проверки, что пользователь является владельцем объекта.
    """

    def test_func(self):
        # Получаем объект
        obj = self.get_object()

        # Проверяем, что объект существует и пользователь является владельцем
        if hasattr(obj, 'owner') and obj.owner == self.request.user:
            return True

        # Если проверка не пройдена, выбрасываем исключение
        raise PermissionDenied("У вас нет прав для выполнения этого действия.")