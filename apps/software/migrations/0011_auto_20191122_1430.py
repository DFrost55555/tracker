# Generated by Django 2.1.10 on 2019-11-22 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_customercontact_custcontact_role'),
        ('software', '0010_softwarematrix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softwarematrix',
            name='swmtx_swvend_fk',
        ),
        migrations.AddField(
            model_name='softwarematrix',
            name='swmtx_cust_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Customer', verbose_name='Customer'),
        ),
    ]
