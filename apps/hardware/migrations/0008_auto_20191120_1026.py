# Generated by Django 2.1.10 on 2019-11-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0007_auto_20191120_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='hw_see_txt',
            field=models.CharField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, max_length=10, null=True, verbose_name='Support End Estimated'),
        ),
    ]
