# Generated by Django 2.1.10 on 2019-11-20 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0006_truefalse_yesno'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalStatus',
            fields=[
                ('apprsts_id', models.AutoField(primary_key=True, serialize=False)),
                ('apprsts_text', models.CharField(max_length=10, verbose_name='Approval Status')),
                ('apprsts_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('apprsts_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('apprsts_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('apprsts_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apprsts_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareFrequency',
            fields=[
                ('swfreq_id', models.AutoField(primary_key=True, serialize=False)),
                ('swfreq_text', models.CharField(max_length=10, verbose_name='Approval Status')),
                ('swfreq_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swfreq_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swfreq_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swfreq_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swfreq_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
