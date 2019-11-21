# Generated by Django 2.1.10 on 2019-11-21 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0008_auto_20191121_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='sw_repl_vend_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swvend_repl_vend_id', to='software.SoftwareVendor', verbose_name='Replacement Software Vendor'),
        ),
        migrations.AlterField(
            model_name='software',
            name='sw_vend_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='software.SoftwareVendor', verbose_name='Software Vendor'),
        ),
        migrations.AlterField(
            model_name='softwarevendor',
            name='swvend_name',
            field=models.CharField(max_length=150, verbose_name='Software Vendor Name'),
        ),
    ]