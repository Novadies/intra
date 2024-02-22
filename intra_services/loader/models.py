from dataclasses import field
from typing import Type, Any, Tuple

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from django.conf import settings
from django.db import models

from loader.validators import Item, Item1

_testmodel = [
    "numberlist", "id_fabrics", "id_work", "id_insta", "id_contract", "id_execut", "id_object", "id_cat", "id_med",

    "otherflange", "rectanga", "rectangb", "id_press", "id_presan", "hydratestpress", "workpress", "opertemp",
    "calcpress",
    "calctemp", "flan1", "materialf1", "dentdeff1", "protectcover", "protectcover1", "defflan1", "transdeff1",
    "longdeff1",
    "ulcercorf1", "wearsurff1", "violgeomf1", "seasurff1", "whyf", "whyf1", "flan2", "materialf2", "dentdeff2",
    "defflan2",
    "transdeff2", "longdeff2", "ulcercorf2", "wearsurff2", "violgeomf2", "seasurff2", "typesurf", "typesurfANSI",
    "diffdesig",
    "diffdesig1", "typegasket", "gasket1", "gasketoht", "gasket2", "gasket3", "gasket4", "gasket5", "gasket6",
    "gasket7",
    "gasketdiam", "gasketwidth", "gasketthick", "clampedpart", "typefast", "threadpitch", "threadpitchansi",
    "fastmater",
    "fastener_vid_inst", "fastinstdiam", "fastinstdiamansi", "fastinstlen", "fastener_vid_need", "fastneeddia",
    "fastneeddiansi",
    "fastneedlen", "numberfast", "fastreject", "fastrepl", "fastrecom", "fastcondit", "deffast1", "deffast2",
    "deffast3",
    "deffast4", "mnogo", "inconsist1", "inconsist2", "inconsist3", "inconsist4", "inconsist5", "inconsist6",
    "inconsist7",
    "inconsist8", "inconsist9", "inconsist10", "typenut", "lubricfast", "tightshem1", "tightshem2", "lubricfast1",
    "tighttorq", "loosefast", "remarkfast1", "remfastdate1", "remarkfast2", "remfastdate2", "coaxiality", "coaxiality1",
    "parallel", "parallel1", "tools", "succgidro", "countgidro", "dategidro", "commgidro", "tag1", "tag2", "usesiz",
    "workingtool", "generalquest", "reactremark", "mechanic", "datemech", "supervisor", "datesuper", "commcheck1",
    "commcheck", "sxemafile", "edit", "created"
]

_testmodel1 = ["rectangular", "flanconnect", "flanthick", "dismantling", "mounting", "gostansi", "different", "id_diam",
               "id_diamsi", ]


class TestModel(models.Model):
    for _i in _testmodel:
        locals()[_i] = models.CharField(
            max_length=99, blank=True)

    def __str__(self):
        return self.id


class TestModel1(models.Model):
    for _i in _testmodel1:
        locals()[_i] = models.CharField(
            max_length=99, blank=True)

    def __str__(self):
        return self.id


MODEL_VALIDATOR = ((TestModel, Item),
                   (TestModel1, Item1))


##############################################################################
@dataclass
class Aggregator:
    """ Агрегатор классов для записи в бд. Кортеж, содержащий кортежи из пар джанго-модель
     и соответствующий валидатор из пайдентик """
    mytuple: Tuple[Tuple[Type[models.Model], Type[BaseModel]], ...]


aggregator = Aggregator(MODEL_VALIDATOR)


class UploadFiles(models.Model):
    file_to_upload = models.FileField(upload_to='uploads', null=True)
    time = models.DateTimeField(auto_now_add=True)
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="upload_files",
        null=True,
    )
