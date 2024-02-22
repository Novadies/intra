from django.contrib import admin

from loader.models import UploadFiles


@admin.register(UploadFiles)
class Upload(admin.ModelAdmin):
    readonly_fields = ["file_to_upload", 'time']
    list_display = ("file_to_upload", 'time')
    list_per_page = 100
    #actions = ["something"]
    search_fields = ["file_to_upload", ]
    date_hierarchy = 'time'

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def delete_model(self, request, obj):
        """
        Переопределение метода delete_model для определения специфического поведения при массовом удалении.
        """
        for item in obj:
            # Ваша логика удаления объекта item
            item.delete()

        return super().delete_model(request, obj)


    # def get_actions(self, request):
    #     """ Скрываем actions для пользователей без определённых разрешений"""
    #     actions = super().get_actions(request)
    #     perm = 'auth.view_user', 'auth.change_user'  # необходимые разрешения или @admin.action(permissions=["change"])
    #     actions_disabled =[]                                       # запрещённые action
    #     if not request.user.has_perm(*perm):
    #         actions = {k: v for k, v in actions.items() if k not in actions_disabled}
    #     return actions