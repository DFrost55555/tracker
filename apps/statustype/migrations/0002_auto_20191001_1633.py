# Generated by Django 2.1.10 on 2019-10-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statustype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statustype',
            name='statustype_modifieddate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]