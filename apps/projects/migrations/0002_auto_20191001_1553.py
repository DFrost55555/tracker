# Generated by Django 2.1.10 on 2019-10-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_modifieddate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]