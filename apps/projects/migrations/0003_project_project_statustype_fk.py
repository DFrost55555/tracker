# Generated by Django 2.1.10 on 2019-09-30 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statustype', '0001_initial'),
        ('projects', '0002_auto_20190930_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_statustype_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statustype.StatusType', verbose_name='Status'),
        ),
    ]
