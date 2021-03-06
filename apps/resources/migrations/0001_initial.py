# Generated by Django 2.1.10 on 2019-10-07 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('res_firstname', models.CharField(max_length=100, verbose_name='firstname')),
                ('res_lastname', models.CharField(max_length=100, verbose_name='lastname')),
                ('res_emp_ref', models.CharField(max_length=50, verbose_name='employee reference')),
                ('res_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('res_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('res_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('res_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='res_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('restype_id', models.AutoField(primary_key=True, serialize=False)),
                ('restype_name', models.CharField(max_length=100, verbose_name='resource type')),
                ('restype_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('restype_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('restype_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('restype_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restype_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='res_resource_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.ResourceType', verbose_name='resource type'),
        ),
    ]
