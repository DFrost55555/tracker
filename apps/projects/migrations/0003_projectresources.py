# Generated by Django 2.1.10 on 2019-10-07 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('statustype', '0002_auto_20191001_1633'),
        ('projects', '0002_auto_20191001_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectResources',
            fields=[
                ('pr_id', models.AutoField(primary_key=True, serialize=False)),
                ('pr_project_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project', verbose_name='project')),
                ('pr_resource_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.Resource', verbose_name='resource')),
                ('pr_statustype_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statustype.StatusType', verbose_name='res status')),
            ],
        ),
    ]
