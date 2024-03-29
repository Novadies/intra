# Generated by Django 4.2.9 on 2024-02-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loader", "0005_uploadfiles_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestModel1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rectangular", models.CharField(blank=True, max_length=99)),
                ("flanconnect", models.CharField(blank=True, max_length=99)),
                ("flanthick", models.CharField(blank=True, max_length=99)),
                ("dismantling", models.CharField(blank=True, max_length=99)),
                ("mounting", models.CharField(blank=True, max_length=99)),
                ("gostansi", models.CharField(blank=True, max_length=99)),
                ("different", models.CharField(blank=True, max_length=99)),
                ("id_diam", models.CharField(blank=True, max_length=99)),
                ("id_diamsi", models.CharField(blank=True, max_length=99)),
            ],
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="different",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="dismantling",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="flanconnect",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="flanthick",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="gostansi",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="id_diam",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="id_diamsi",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="mounting",
        ),
        migrations.RemoveField(
            model_name="testmodel",
            name="rectangular",
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="calcpress",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="calctemp",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="clampedpart",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="coaxiality",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="coaxiality1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="commcheck",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="commcheck1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="commgidro",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="countgidro",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="created",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="dategidro",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="datemech",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="datesuper",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="deffast1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="deffast2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="deffast3",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="deffast4",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="defflan1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="defflan2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="dentdeff1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="dentdeff2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="diffdesig",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="diffdesig1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="edit",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastcondit",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastener_vid_inst",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastener_vid_need",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastinstdiam",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastinstdiamansi",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastinstlen",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastmater",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastneeddia",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastneeddiansi",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastneedlen",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastrecom",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastreject",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="fastrepl",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="flan1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="flan2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasket1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasket2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasket3",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasket4",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasket5",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasket6",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasket7",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasketdiam",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasketoht",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasketthick",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="gasketwidth",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="generalquest",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="hydratestpress",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_cat",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_contract",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_execut",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_fabrics",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_insta",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_med",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_object",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_presan",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_press",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="id_work",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist10",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist3",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist4",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist5",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist6",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist7",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist8",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="inconsist9",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="longdeff1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="longdeff2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="loosefast",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="lubricfast",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="lubricfast1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="materialf1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="materialf2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="mechanic",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="mnogo",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="numberfast",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="numberlist",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="opertemp",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="otherflange",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="parallel",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="parallel1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="protectcover",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="protectcover1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="reactremark",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="rectanga",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="rectangb",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="remarkfast1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="remarkfast2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="remfastdate1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="remfastdate2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="seasurff1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="seasurff2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="succgidro",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="supervisor",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="sxemafile",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="tag1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="tag2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="threadpitch",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="threadpitchansi",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="tightshem1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="tightshem2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="tighttorq",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="tools",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="transdeff1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="transdeff2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="typefast",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="typegasket",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="typenut",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="typesurf",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="typesurfANSI",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="ulcercorf1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="ulcercorf2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="usesiz",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="violgeomf1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="violgeomf2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="wearsurff1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="wearsurff2",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="whyf",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="whyf1",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="workingtool",
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AlterField(
            model_name="testmodel",
            name="workpress",
            field=models.CharField(blank=True, max_length=99),
        ),
    ]
