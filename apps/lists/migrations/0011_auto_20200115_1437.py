# Generated by Django 2.1.10 on 2020-01-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0010_listimpact_listseverity_liststatus_riskimpact_risklikelihood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listimpact',
            name='ltimpact_score',
            field=models.IntegerField(verbose_name='list impact score'),
        ),
        migrations.AlterField(
            model_name='listseverity',
            name='ltsev_score',
            field=models.IntegerField(verbose_name='list severity score'),
        ),
        migrations.AlterField(
            model_name='riskimpact',
            name='rskimpact_score',
            field=models.IntegerField(verbose_name='risk impact score'),
        ),
        migrations.AlterField(
            model_name='risklikelihood',
            name='rsklklh_score',
            field=models.IntegerField(verbose_name='risk likelihood score'),
        ),
    ]
