# Generated by Django 2.1.10 on 2020-01-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purorders', '0009_auto_20200115_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
