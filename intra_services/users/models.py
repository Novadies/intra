from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Q
from django.forms import DateInput

from model_utils import Choices
from model_utils.fields import StatusField, UrlsafeTokenField, MonitorField
from phonenumber_field.modelfields import PhoneNumberField
from functools import wraps
from pathlib import Path
from typing import Optional, Tuple
from ckeditor_uploader.fields import RichTextUploadingField
from sortedm2m.fields import SortedManyToManyField

def decorator_user_directory_path(folders: Optional[Tuple] = None, base_folder: str = 'users'):
    """ Декоратор для user_directory_path ля передачи произвольного числа папок """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs, base_folder=base_folder, folders=folders)
            return result
        return wrapper
    return decorator


def user_directory_path(instance, filename, base_folder=None, folders=None) -> Path:
    """ адрес для сохранения файлов, используя путь от рут + от нуля папок. Работает в связке с декоратором.
    base_folder первая папка после корня, по умолчанию users, см декоратор.
    filename имя файла, это уже не папка
    """
    base = Path(base_folder) / instance.to_user.username
    return base / Path(*folders, filename) if folders else base / filename


###################################################################################################
class CustomUserManager(UserManager):
    """ кастомный юзер. Cоздан метод на основе get_by_natural_key и дополняет его"""

    def get_by_natural_key_v2(self, username):
        """ используется кастомный ALL_USERNAME_FIELD """
        all_fields = getattr(self.model, "ALL_USERNAME_FIELD", None)
        if all_fields is not None:
            conditions = Q()
            for field in all_fields:
                conditions |= Q(**{field: username})
            return self.get(conditions)
        else:
            return self.get_by_natural_key(username)


class User(AbstractUser):
    """ дополнение базового юзера """
      class Meta:
        indexes = [
            models.Index(fields=['username', 'telefon_number', 'first_name', 'last_name', 'position']),
        ]
    objects = CustomUserManager()
    # todo возможно профессии должны быть в бд. Для того что бы была возможность добавлять новые у персонала, например
    POSITION = Choices(
        ('nd', 'Нет данных'),
        ('engineer1', 'Инженер I категории'),
        ('engineer2', 'Инженер II категории'),
        ('engineer3', 'Инженер III категории'),
    )
    is_active.verbose_name = "Действующий сотрудник?"
    email = models.EmailField(unique=True, null=True)
    patronymic = models.CharField(max_length=99, blank=True, db_index=True, verbose_name='Отчество')
    personal_number = models.PositiveIntegerField(unique=True, null=True, verbose_name='Табельный номер')
    position = StatusField(choices_name='POSITION', verbose_name='Должность')     # null=True,
    position_rate = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Ставка')
    change_rate = MonitorField(monitor='position_rate', verbose_name='Дата последнего изменения ставки')
    # todo с номерами тоже самое. Возможно для них должна быть отдельная таблица
    telefon_number = PhoneNumberField(blank=True)
    uuid = UrlsafeTokenField(editable=False, max_length=128, null=True)  # todo Токен/ по заказу Николая. хз нах нужен

    REQUIRED_FIELDS = ['username']                    # обязательные поля
    USERNAME_FIELD = 'email'                          # для логина используется 
    ALL_USERNAME_FIELD = 'email', 'username'          # это кастомная константа, имеет приоритет перед USERNAME_FIELD

    def __str__(self):
        return f"{self.last_name} {self.first_name or ''}" if self.last_name else self.username

    def save(self, *args, **kwargs):
        """ Иначе email будут пустыми, что выкинет ошибку """
        fields_to_check = ['email']
        for field in fields_to_check:
            if getattr(self, field) == "":
                setattr(self, field, None)
        super().save(*args, **kwargs)


class UserExtraField(models.Model):
    """ расширение модели юзера """
    EDUCATION = Choices(
        ('nd', 'Нет данных'),
        ('higher', 'Высшее'),
        ('medium', 'Среднее'),
    )

    # votes = models.PositiveIntegerField(default=0)
    about_user = RichTextUploadingField(blank=True, verbose_name="Комментарии о сотруднике")
    photo = models.ImageField(upload_to=decorator_user_directory_path()(user_directory_path),
                              blank=True, null=True, verbose_name="Путь к фото")
    date_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    data_job = models.DateField(blank=True, null=True, verbose_name="Дата приёма на работу")
    email_private = models.EmailField(blank=True, null=True, verbose_name="Личная почта")
    education = StatusField(choices_name='EDUCATION', verbose_name='Образование')  # blank=True,
    address = models.CharField(max_length=199, blank=True, verbose_name='Адрес проживания')

    to_user = models.OneToOneField(
        "User",
        primary_key=True,  # to_user будет ключом
        on_delete=models.CASCADE,
        unique=True,
        related_name="user_extra_field",
    )

    def __str__(self):
        return ''


class UserLicencesField(models.Model):
    """ Корочки и удостоверения """
    upload_folder = ['Корочки по охране труда', 'Удостоверения']

    DOC1 = (('safety', 'Охрана труда'),
            ('first_aid', 'Первая помощь'),
            ('prom_bez', 'Промышленная безопасность'),
            ('electrical', 'Электробезопасность'),
            ('height', 'Работа на высоте'),
            ('ciz', 'Применение СИЗ'),
            ('gas_work', 'Газоопасные работы'))

    DOC2 = (('pvk', 'ПВК'),
            ('vic', 'ВИК'),
            ('uzk', 'УЗК'),
            ('naks', 'НАКС'),
            ('rfa', 'РФА'))

    for folder, DOC in zip(upload_folder, [DOC1, DOC2]):
        for code, label in DOC:
            locals()[code] = models.CharField(max_length=250, blank=True, verbose_name=label)
            locals()[f'{code}_scan'] = models.FileField(
                upload_to=decorator_user_directory_path(folders=(folder,))(user_directory_path),
                blank=True, null=True, verbose_name=f'{label} скан')
            locals()[f'{code}_date_start'] = models.DateField(blank=True, null=True,
                                                              verbose_name=f'{label}: дата получения удостоверения')
            locals()[f'{code}_data_stop'] = models.DateField(blank=True, null=True,
                                                             verbose_name=f'{label}: дата окончания действия')

    to_user = models.OneToOneField(
        "User",
        primary_key=True,  # to_user будет ключом
        on_delete=models.CASCADE,
        unique=True,
        related_name="user_licences_field",
    )

    def __str__(self):
        return ''

class Competency(models.Model):
    """ Компетенции персонала(виды) """
    competence = models.CharField(max_length=99, unique=True, blank=True, null=True, verbose_name='Компетенции')
    requirements = models.CharField(max_length=250, unique=True, blank=True, null=True, verbose_name='Требования к кандидатам')

    to_user = models.ManyToManyField(
        "User",
        related_name="user_competence",
        through='CompetencyAmongUser'
    )
    
    def __str__(self):
        return f'{competence}'

class CompetencyAmongUser(models.Model):
    """ Промежуточная модель для Competency и User """
    competency = models.ForeignKey('Competency', on_delete=models.CASCADE,)
    user = models.ForeignKey("User", on_delete=models.CASCADE,)
    # to_project = models.ManyToManyField(
    #     "Project",
    #     related_name="user_competence",
    # )

class Project(models.Model):
    """ Модель проекта, соединяется с промежуточной моделью CompetencyAmongUser, но не напрямую с User """
    
    # todo: Для модели супервайзинга возможно целесообразно использовать древовидную структуру и соотвественно mptt или глубина вложенности слишком мала что бы был смысл?
    
    BOOL = Choices(
        ('action', 'В процессе'),
        ('complet', 'Завершён'),
    )
    """ пример: руководитель руководит разными проектами (тут не имеет разницы что проекты могут совпадать по времени, для этого реализовывается валидация) по этому внешний ключ 
    """
    @staticmetod
    def get_choices():
        
        return {}
    # todo: для проекта необходимо реализовать добавление требуемых компетенций, и соответственно выбор персонала должно быть отфильтровано на этом основании
    leader = models.ForeignKey("CompetencyAmongUser", on_delete=models.PROTECT, limit_choices_to=self.get_choices())   
    # deputy = models.ForeignKey("CompetencyAmongUser", on_delete=models.PROTECT,)  # каковы компетенции зама?
    personal = models.ManyToManyField("CompetencyAmongUser", on_delete=models.PROTECT, )
    # manadger = StatusField(choices_name='MANADGERS', verbose_name='Менеджеры')  # todo: менеджеры должны быть в бд
    
    code = models.CharField(max_length=99, blank=True, verbose_name='Шифр проекта')
    place = models.CharField(max_length=99, blank=True, verbose_name='Локация')
    plant = models.CharField(max_length=99, blank=True, verbose_name='Предприятие')
    start = models.DateField(blank=True, null=True, verbose_name="Дачало проекта")
    # todo: у проекта ставится дата завершения когда меняется его статус. Если даты выставлена, а потом поменян статус дата обновится, что может быть не то что ожидается.
    stop = MonitorField(monitor='status', verbose_name='Дата завершения проекта') 
    status =  StatusField(choices_name='BOOL', verbose_name='Статус проекта') 
    
    def __str__(self):
        return f'{code}   {place or ''}'
    
