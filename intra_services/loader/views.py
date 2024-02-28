from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView

from loader.forms import UploadFileForm
from loader.tools.logic import save_file
from logs.logger import log_apps


class FileLoader(LoginRequiredMixin, FormView):
    """ Здесь обрабатываются POST запросы"""
    form_class = UploadFileForm
    model = form_class.Meta.model
    # template_name = "loader/upload_form2.html"

    def form_valid(self, form):
        try:
            local_instance = self.local_instance
        except AttributeError:
            local_instance = None

        uploaded_files = form.cleaned_data['file_to_upload']
        """ Ловля ошибок здесь нужна только для того что бы редиректить на определённые страницы, если есть надобность """
        try:
            save_file(self, uploaded_files, local_instance)     # сюда нужно передавать экземпляр DB_ExcelEntry
        except FileNotFoundError:
            # Обработка ошибки, когда файл не найден
            return HttpResponseRedirect(self.request.path)
        except PermissionError:
            # Обработка ошибки, когда нет прав на запись
            return HttpResponseRedirect(self.request.path)
        except Exception:
            return HttpResponseRedirect(self.request.path)
        return HttpResponseRedirect(self.request.path)
