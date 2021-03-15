from rest_framework.permissions import BasePermission


class IQCommentPermissions(BasePermission):
    def has_permission(self, request, view):
        """
        # first check


        user_group = self.check_user_group(request)

        # also
        # ...
        if request.user.is_superuser:
            return True
        :param self:
        :param request:
        :param view:
        :return:
        """

        return True
