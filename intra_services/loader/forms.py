from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.validators import FileExtensionValidator, MaxLengthValidator

from loader.models import UploadFiles


#
# class ContactForm(forms.Form):
#     """ Форма обратной связи, посылает сообщение на почту юзеру и сама себе """
#     name = forms.CharField(label='Имя', max_length=255)
#     email = forms.EmailField(label='Email')
#     content = forms.CharField(label='', widget=CKEditorUploadingWidget())
#     captcha = ReCaptchaField(label='')


class UploadFileForm(forms.ModelForm):
    file_to_upload = forms.FileField(label='Выберите файл', required=True,
                                     widget=forms.FileInput(attrs={'accept': '.xlsx,.xlsm',
                                                                   # .csv', # todo  csv пока не читаем
                                                                   'id': 'exel_files'}),
                                     validators=[  # MaxLengthValidator(max_size=5242880),
                                         # FileExtensionValidator(allowed_extensions= ['xlsx', 'xlsm', 'csv']),
                                     ],
                                     )

    class Meta:
        model = UploadFiles
        fields = ['file_to_upload']
