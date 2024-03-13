import datetime
import warnings

from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError

from ckeditor.widgets import CKEditorWidget
from phonenumber_field.formfields import PhoneNumberField

from loader.forms import UploadFileForm
from logs.logger import debug
from users.models import UserLicencesField
from users.tool.logic import true_or_None


class LoginUserForm(AuthenticationForm):
    """ Форма входа """

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'})
        }
        labels = {
            'username': 'Логин',
            'password': 'Пароль'
        }
        error_messages = {
            'username': {
                'invalid': 'Логин или пароль неверны'
            },
            'password': {
                'required': 'Логин или пароль неверны.'
            }
        }
        help_texts = {
            'username': 'Не забывайте про регистр',
        }


class RegisterUserForm(UserCreationForm):
    """ Форма регистрации """
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']  # убрал поля
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        field = 'email'
        email = self.cleaned_data[field]
        if self.Meta.model.objects.filter(email=email).exists():
            self.add_error(field, ValidationError("Такой E-mail уже существует!"))
        return email


class UserForm(UserChangeForm):
    """ Добавлена валидация для админки по модели User """
    def clean(self):   # todo настроить валидацию/  целом валидировать нечего вроде
        if False: raise forms.ValidationError("A Всё хуйня")

class ProfileUserForm(forms.ModelForm):      # todo настроить профиль юзера
    """ Форма профиля пользователя"""
    this_year = datetime.date.today().year

    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail')
    position = forms.CharField(disabled=True, label='Должность')
    telefon_number = PhoneNumberField()
    """ формы вне модели user """
    data_job = forms.DateField(disabled=True)
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))))
    email_private = forms.CharField(label='личный E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # about_user = forms.CharField(required=False, widget=CKEditorWidget(), )
    photo = forms.ImageField(label='Выберите фото', widget=forms.FileInput(attrs={'accept': 'image/*'}), required=False)
    education = forms.CharField(label='Образование', widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Адрес проживания', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'patronymic']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'patronymic': 'Отчество'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean(self):
        """ Удаляяем поля формы определённые как disabled из сохраняемых """
        self.cleaned_data = {field: self.cleaned_data[field] for field
                             in self.cleaned_data.keys() if not self.fields[field].disabled}
        fields_to_check = ['email']
        self.cleaned_data = true_or_None(self.cleaned_data, fields_to_check)


class UserPasswordChangeForm(PasswordChangeForm):
    """ Форма смены пароля """
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля",
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class LicenceFileLoader(forms.ModelForm): # todo удалить если будет удалено представление
    """ базовый класс в котором определяется форма для загрузки"""
    class Meta:
        model = UserLicencesField
        _fields = model.DOC1 + model.DOC2
        fields = [field[0] for field in _fields]
        widgets = {
            field: forms.FileInput(
                attrs={'accept': '.pdf,.doc',  # todo хз какие тут расширения должны быть
                       'id': 'licence_files'}
            )
            for field in fields
        }
        labels = {field[0]: field[1] for field in _fields}
