# Generated by Django 2.1.10 on 2019-11-04 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0003_listpriority_poitemtype_ragstatus_raidstatus_raidtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardwareCategory',
            fields=[
                ('hwcat_id', models.AutoField(primary_key=True, serialize=False)),
                ('hwcat_name', models.CharField(max_length=150, verbose_name='hardware category name')),
                ('hwcat_description', models.CharField(max_length=2000, verbose_name='hardware category description')),
                ('hwcat_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('hwcat_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('hwcat_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('hwcat_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hwcat_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareStatus',
            fields=[
                ('hwsts_id', models.AutoField(primary_key=True, serialize=False)),
                ('hwsts_name', models.CharField(max_length=150, verbose_name='hardware status name')),
                ('hwsts_description', models.CharField(max_length=2000, verbose_name='hardware status description')),
                ('hwsts_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('hwsts_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('hwsts_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('hwsts_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hwsts_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareCategory',
            fields=[
                ('swcat_id', models.AutoField(primary_key=True, serialize=False)),
                ('swcat_name', models.CharField(max_length=150, verbose_name='software category name')),
                ('swcat_description', models.CharField(max_length=2000, verbose_name='software category description')),
                ('swcat_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swcat_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swcat_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swcat_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swcat_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareClassification',
            fields=[
                ('swclass_id', models.AutoField(primary_key=True, serialize=False)),
                ('swclass_name', models.CharField(max_length=150, verbose_name='software classification  name')),
                ('swclass_description', models.CharField(max_length=2000, verbose_name='software classification description')),
                ('swclass_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swclass_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swclass_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swclass_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swclass_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareStatus',
            fields=[
                ('swsts_id', models.AutoField(primary_key=True, serialize=False)),
                ('swsts_name', models.CharField(max_length=150, verbose_name='software status name')),
                ('swsts_description', models.CharField(max_length=2000, verbose_name='software status description')),
                ('swsts_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swsts_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swsts_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swsts_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swsts_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]