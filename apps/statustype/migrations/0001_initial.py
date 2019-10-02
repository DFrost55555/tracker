# Generated by Django 2.1.10 on 2019-09-30 15:47

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
            name='StatusType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statustype_name', models.CharField(max_length=150, verbose_name='Service Area Name')),
                ('statustype_description', models.CharField(max_length=2000, verbose_name='Description')),
                ('statustype_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('statustype_modifieddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('statustype_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('statustype_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statustype_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]