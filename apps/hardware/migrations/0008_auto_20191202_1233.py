# Generated by Django 2.1.10 on 2019-12-02 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0007_auto_20191202_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwarematrix',
            name='hwmtx_cust_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Customer', verbose_name='Hardware Customer'),
        ),
    ]
