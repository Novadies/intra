from .forms import ThisAppUploadFileForm
from .tools.save_to_db_class import instance_DB_ExcelEntry
from loader.views import FileLoader


class PsevdoFileLoader(FileLoader):
    form_class = ThisAppUploadFileForm
    template_name = "example_something_app/sheet_with_upload_form.html"
    local_instance = instance_DB_ExcelEntry     # передаём экземпляр DB_ExcelEntry
