# Generated by Django 2.1.10 on 2019-10-08 12:56

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
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100, verbose_name='role name')),
                ('role_desc', models.CharField(max_length=2000, verbose_name='role description')),
                ('role_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('role_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('role_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('role_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='role_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]