from rest_framework.permissions import BasePermission


class IQBoardPermissions(BasePermission):
    def has_permission(self, request, view):
        user_group = self.check_user_group(request)
        if request.user.is_superuser:
            return True

        # her halukarda diyelim simdilik
        return True

    def check_user_group(self, request):
        """
        Gruplar acilmadan bunu kullanmayalim.
        :param request:
        :return:
        """
        if request.user and request.user.groups.filter(name='BoardEditors'):
            return True

        return False
