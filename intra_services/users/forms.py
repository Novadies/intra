import datetime
import warnings

from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError

from ckeditor.widgets import CKEditorWidget

from logs.logger import debug
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
        fields = ['username', 'email', 'password1', 'password2'] # убрал поля
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
    """ Форма для CustomUserAdmin.
        Можно внести дополнительные поля, не связанные с моделью и соответственные методы.
    """
    pass

class ProfileUserForm(forms.ModelForm):
    """ Форма профиля пользователя"""
    this_year = datetime.date.today().year

    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))

    """ формы вне модели user """
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))))
    about_user = forms.CharField(widget=CKEditorWidget(), required=False)
    photo = forms.ImageField(label='Выберите фото', widget=forms.FileInput(attrs={'accept': 'image/*'}), required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
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
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

