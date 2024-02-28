from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from example_something_app.forms import ThisAppUploadFileForm
from example_something_app.tools.for_save_to_db_CLASS import instance_DB_ExcelEntry
from loader.views import FileLoader


class PsevdoFileLoader(LoginRequiredMixin, View):
    """ вьюха разделяется на 2. Для обработки отдельно post и get запросов """
    def get(self, request, *args, **kwargs):
        view = PsevdoFile.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AppFileLoader.as_view()
        return view(request, *args, **kwargs)


class AppFileLoader(FileLoader):
    local_instance = instance_DB_ExcelEntry     # необходимо передать экземпляр класса загрузчика


class PsevdoFile(LoginRequiredMixin, FormView):
    form_class = ThisAppUploadFileForm
    template_name = "example_something_app/sheet_with_upload_form.html"
    #model = form_class.Meta.model

    # def get_initial(self):
    #     """ Начальные значения для формы """
    #     initial = super().get_initial()
    #     return initial
