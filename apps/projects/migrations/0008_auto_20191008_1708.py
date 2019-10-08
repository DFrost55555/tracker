# Generated by Django 2.1.10 on 2019-10-08 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('projects', '0007_auto_20191008_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectresources',
            name='pr_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Cost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectresources',
            name='pr_end_date',
            field=models.DateField(null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='projectresources',
            name='pr_role_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roles.Role', verbose_name='resource role'),
        ),
        migrations.AddField(
            model_name='projectresources',
            name='pr_start_date',
            field=models.DateField(null=True, verbose_name='Start Date'),
        ),
        migrations.AddField(
            model_name='projectresources',
            name='pr_xcharge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='XCharge'),
            preserve_default=False,
        ),
    ]
