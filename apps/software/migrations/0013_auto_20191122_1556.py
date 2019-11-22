# Generated by Django 2.1.10 on 2019-11-22 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0012_auto_20191122_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swvendorcontact',
            name='swvendcontact_vend_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='software.SoftwareVendor', verbose_name='Software Vendor'),
        ),
        migrations.AlterField(
            model_name='swvendornote',
            name='swvendnote_vend_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='software.SoftwareVendor', verbose_name='Software Vendor'),
        ),
    ]
