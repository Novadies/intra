from typing import Tuple

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from more_itertools import collapse
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple

from users.forms import RegisterUserForm, UserForm
from users.models import User, UserExtraField, UserLicencesField, Competency, CompetencyAmongUser

admin.site.unregister(Group)


@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    """ Запрет на создание и тд групп (в частости Группы), в том числе с правами пользователя """

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser



class CompetencyInline(admin.TabularInline):
    model = CompetencyAmongUser
    extra = 1
    verbose_name_plural = "Компетенции сотрудника"
    verbose_name = "вид компетенции"

    # filter_horizontal = ("competence_id", 'to_user')


class ExtraUserInline(admin.StackedInline):
    can_delete = False
    model = UserExtraField
    verbose_name = 'Дополнительные поля пользователя'
    empty_value_display = ''
    readonly_fields = ['get_photo']

    # radio_fields = {"education": admin.VERTICAL}

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 300px;">') if obj.photo.url else None

    get_photo.short_description = 'Фотография'

    fieldsets = (
        ('Фотография сотрудника', {'fields': ('photo', 'get_photo'), 'classes': ['collapse']}),  # 'votes',
        ('О пользователе', {'fields': ('date_birth', 'data_job', 'email_private', 'education', 'address', 'about_user'),
                            'classes': ['collapse']}),
    )


class LicencesUserInline(admin.StackedInline):
    can_delete = False
    model = UserLicencesField
    verbose_name = 'Удостоверения пользователя'

    @staticmethod
    def collapses(doc: Tuple) -> list:
        """ Подготавливает список для передачи в fieldsets """
        f = [[code, (f'{code}_date_start', f'{code}_data_stop'), f'{code}_scan'] for code, _ in doc]
        return list(collapse(f, base_type=tuple))

    def get_fieldsets(self, request, obj=None):
        return [
            (upload_folder, {'fields': self.collapses(DOC), 'classes': ['collapse']})
            for upload_folder, DOC in zip(self.model.upload_folder, [self.model.DOC1, self.model.DOC2])
        ]
@admin.register(CompetencyAmongUser)
class Competency_AmongUser(admin.ModelAdmin):
    list_display = ['competency', 'user']

@admin.register(Competency)
class Competency_in_admin(admin.ModelAdmin):
    fieldsets = (('Компетенции', {'fields': ('competence', 'requirements')}),)
    list_display = ['competence', 'requirements']
    inlines = [CompetencyInline]
    # filter_horizontal = ("competence_id", 'user_id')


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """ Головная форма отображения юзеров"""
    form = UserForm
    add_form = RegisterUserForm  # здесь нужно просто указать свою форму регистрации наследуемую от UserCreationForm
    model = get_user_model()  # по идее переопределяет form.Meta.User, лучше не удалять на всякий случай
    list_display = ['last_name', 'first_name', 'patronymic',
                    'case_name',
                    'email', 'telefon_number', 'username',
                    'is_staff']  # отображение в корневой папке Пользователи
    # readonly_fields = []
    # list_select_related = True
    list_display_links = ('case_name', 'email', 'username')
    search_fields = ['case_name', 'email', 'telefon_number', 'username']
    # date_hierarchy = 'поле'
    # filter_horizontal = (
    #     "groups",
    #     "user_permissions",
    # )
    list_per_page = 150

    inlines = (ExtraUserInline, LicencesUserInline, CompetencyInline)
    fieldsets = (
        ('ФИО', {'fields': ('first_name', 'patronymic', 'last_name')}),
        ('Основные данные', {'fields': ('username', 'password', 'email', 'telefon_number'),
                             'classes': ['collapse']}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                   'classes': ['collapse']}),
        ('Должность', {'fields': ('position', 'position_rate', 'change_rate'),
                       'classes': ['collapse']}),
        ('Даты пользователя', {'fields': ('last_login', 'date_joined'), 'classes': ['collapse']}),
    )

    @admin.display(description="Имя")
    def case_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def get_readonly_fields(self, request, obj=None):
        """ Запретить пользователям, не являющимся суперпользователями,
        редактировать свои и чужие разрешения и группы разрешений,
        а так же дополнительные выбранные поля"""
        extra_all_disabled_fields = ()  # запрет на редактирование для Не суперпользователей
        extra_self_disabled_fields = ('username',)  # запрет на редактирование своих полей
        extra_staff_disabled_fields = ('groups',)  # запрет на редактирование других staff
        readonly_fields = set(self.readonly_fields)
        if not request.user.is_superuser:  # запрет на изменение прав и полей
            readonly_fields |= {
                'is_superuser',
                'user_permissions',
                'is_staff',
                *extra_all_disabled_fields,
            }
            if obj is not None:  # запрет на редактирование СОБСТВЕННЫХ полей
                if obj == request.user:
                    readonly_fields |= {
                        'groups',
                        *extra_self_disabled_fields,
                    }
                if obj.is_superuser:  # запрет на редактирование superuser
                    readonly_fields |= {
                        'is_active',
                        'username',
                        'email',
                        'groups',
                    }
                if obj.is_staff:  # запрет на редактирование staff
                    readonly_fields |= {
                        'username',
                        'email',
                        *extra_staff_disabled_fields,
                    }
        return readonly_fields

    """ общие разрешения для работы с моделями """

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        """ Скрываем actions для пользователей без определённых разрешений"""
        actions = super().get_actions(request)
        perm = 'auth.view_user', 'auth.change_user'  # необходимые разрешения или @admin.action(permissions=["change"])
        actions_disabled = []  # запрещённые action
        if not request.user.has_perm(*perm):
            actions = {k: v for k, v in actions.items() if k not in actions_disabled}
        return actions
