# Generated by Django 2.1.10 on 2019-11-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0005_auto_20191107_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='hw_see_txt',
            field=models.BooleanField(default=False, verbose_name='Support End Estimated'),
            preserve_default=False,
        ),
    ]
