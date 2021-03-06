# Generated by Django 2.1.10 on 2019-11-20 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20191120_1956'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('software', '0006_auto_20191120_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareVendor',
            fields=[
                ('swvend_id', models.AutoField(primary_key=True, serialize=False)),
                ('swvend_name', models.CharField(max_length=150, verbose_name='Vendor Name')),
                ('swvend_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swvend_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swvend_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swvend_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swvend_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SWVendorContact',
            fields=[
                ('swvendcontact_id', models.AutoField(primary_key=True, serialize=False)),
                ('swvendcontact_firstname', models.CharField(max_length=150, verbose_name='First Name')),
                ('swvendcontact_lastname', models.CharField(max_length=150, verbose_name='Last Name')),
                ('swvendcontact_role', models.CharField(max_length=150, null=True, verbose_name='Role')),
                ('swvendcontact_email', models.EmailField(max_length=250, verbose_name='Email Address')),
                ('swvendcontact_telnum', models.CharField(max_length=150, verbose_name='Telephone Number')),
                ('swvendcontact_mobnumber', models.CharField(max_length=150, verbose_name='Mobile Number')),
                ('swvendcontact_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swvendcontact_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swvendcontact_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swvendcontact_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swvendcontact_editor', to=settings.AUTH_USER_MODEL)),
                ('swvendcontact_vend_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendor', verbose_name='Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='SWVendorNote',
            fields=[
                ('swvendnote_id', models.AutoField(primary_key=True, serialize=False)),
                ('swvendnote_note', models.CharField(max_length=2500, verbose_name='Note')),
                ('swvendnote_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swvendnote_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swvendnote_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swvendnote_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swvendnote_editor', to=settings.AUTH_USER_MODEL)),
                ('swvendnote_vend_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendor', verbose_name='Vendor')),
            ],
        ),
    ]
