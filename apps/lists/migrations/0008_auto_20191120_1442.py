# Generated by Django 2.1.10 on 2019-11-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_approvalstatus_softwarefrequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvalstatus',
            name='apprsts_text',
            field=models.CharField(max_length=50, verbose_name='Approval Status'),
        ),
    ]
