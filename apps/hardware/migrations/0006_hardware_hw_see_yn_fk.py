# Generated by Django 2.1.10 on 2019-11-20 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_truefalse_yesno'),
        ('hardware', '0005_auto_20191107_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='hw_see_yn_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.YesNo', verbose_name='Support End Estimated'),
        ),
    ]