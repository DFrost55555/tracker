# Generated by Django 2.1.10 on 2019-10-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargecodetype',
            name='cct_description',
            field=models.CharField(max_length=2000, verbose_name='charge code type description'),
        ),
        migrations.AlterField(
            model_name='chargecodetype',
            name='cct_name',
            field=models.CharField(max_length=150, verbose_name='charge code type name'),
        ),
        migrations.AlterField(
            model_name='chargeunittype',
            name='cut_description',
            field=models.CharField(max_length=2000, verbose_name='charge unit type description'),
        ),
        migrations.AlterField(
            model_name='chargeunittype',
            name='cut_name',
            field=models.CharField(max_length=150, verbose_name='charge unit type name'),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='prjsts_description',
            field=models.CharField(max_length=2000, verbose_name='project status description'),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='prjsts_name',
            field=models.CharField(max_length=150, verbose_name='project status name'),
        ),
        migrations.AlterField(
            model_name='resourcestatus',
            name='ressts_description',
            field=models.CharField(max_length=2000, verbose_name='resource status description'),
        ),
        migrations.AlterField(
            model_name='resourcestatus',
            name='ressts_name',
            field=models.CharField(max_length=150, verbose_name='resource status name'),
        ),
    ]
