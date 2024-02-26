from itertools import chain
from pathlib import Path

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import View, ListView, FormView, CreateView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from transliterate import slugify

from loader.forms import UploadFileForm
from loader.tools.logic import save_file
from loader.models import TestModel, UploadFiles
from logs.logger import log_apps


class FileLoader(LoginRequiredMixin, FormView):
    form_class = UploadFileForm
    template_name = "loader/upload_form2.html"
    model = form_class.Meta.model

    # def get_initial(self):
    #     """ Начальные значения для формы """
    #     initial = super().get_initial()
    #     return initial

    def form_valid(self, form):
        #save_in_session(self, form, name_in_session='mail_checkbox')

        uploaded_files = form.cleaned_data['file_to_upload']
        """ Ловля ошибок здесь нужна только для того что бы редиректить на определённые страницы, если есть надобность """
        try:
            save_file(self, uploaded_files)
        except FileNotFoundError:
            # Обработка ошибки, когда файл не найден
            return HttpResponseRedirect(reverse('loader:files'))
        except PermissionError:
            # Обработка ошибки, когда нет прав на запись
            return HttpResponseRedirect(reverse('loader:files'))
        except Exception:
            return HttpResponseRedirect(reverse('loader:files'))
        return HttpResponseRedirect(reverse('loader:files'))
