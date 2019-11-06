# Generated by Django 2.1.10 on 2019-11-06 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='hw_ees1_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_ees2_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_ees3_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_ems_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_eow_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_plp_txt',
            field=models.CharField(max_length=250, null=True, verbose_name='Hardware Description'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_repl_desc',
            field=models.CharField(max_length=250, null=True, verbose_name='Replacement Hardware Description'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_repl_vend_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hw_repl_vend_id', to='vendors.Vendor'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_see_txt',
            field=models.CharField(max_length=250, null=True, verbose_name='Hardware Description'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='hw_vend_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendor'),
        ),
    ]
