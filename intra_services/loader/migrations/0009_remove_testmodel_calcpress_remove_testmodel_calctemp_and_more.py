# Generated by Django 4.2.9 on 2024-02-26 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("loader", "0008_uploadfiles_db_record"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testmodel",
            name="calcpress",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="calctemp",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="clampedpart",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="coaxiality",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="coaxiality1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="commcheck",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="commcheck1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="commgidro",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="countgidro",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="created",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="dategidro",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="datemech",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="datesuper",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="deffast1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="deffast2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="deffast3",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="deffast4",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="defflan1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="defflan2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="dentdeff1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="dentdeff2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="diffdesig",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="diffdesig1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="edit",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastcondit",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastener_vid_inst",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastener_vid_need",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastinstdiam",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastinstdiamansi",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastinstlen",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastmater",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastneeddia",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastneeddiansi",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastneedlen",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastrecom",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastreject",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="fastrepl",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="flan1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="flan2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasket1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasket2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasket3",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasket4",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasket5",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasket6",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasket7",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasketdiam",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasketoht",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasketthick",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gasketwidth",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="generalquest",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="hydratestpress",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="id_presan",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="id_press",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist10",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist3",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist4",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist5",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist6",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist7",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist8",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="inconsist9",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="longdeff1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="longdeff2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="loosefast",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="lubricfast",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="lubricfast1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="materialf1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="materialf2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="mechanic",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="mnogo",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="numberfast",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="opertemp",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="otherflange",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="parallel",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="parallel1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="protectcover",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="protectcover1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="reactremark",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="rectanga",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="rectangb",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="remarkfast1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="remarkfast2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="remfastdate1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="remfastdate2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="seasurff1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="seasurff2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="succgidro",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="supervisor",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="sxemafile",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="tag1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="tag2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="threadpitch",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="threadpitchansi",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="tightshem1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="tightshem2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="tighttorq",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="tools",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="transdeff1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="transdeff2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="typefast",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="typegasket",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="typenut",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="typesurf",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="typesurfANSI",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="ulcercorf1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="ulcercorf2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="usesiz",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="violgeomf1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="violgeomf2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="wearsurff1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="wearsurff2",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="whyf",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="whyf1",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="workingtool",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="workpress",
        ),
        migrations.RemoveField(
            model_name="testmodel1",
            name="different",
        ),
        migrations.RemoveField(
            model_name="testmodel1",
            name="id_diam",
        ),
        migrations.RemoveField(
            model_name="testmodel1",
            name="id_diamsi",
        ),
        migrations.AddField(
            model_name="testmodel",
            name="to_uploader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="testmodel",
                to="loader.uploadfiles",
            ),
        ),
        migrations.AddField(
            model_name="testmodel1",
            name="to_uploader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="testmodel1",
                to="loader.uploadfiles",
            ),
        ),
    ]