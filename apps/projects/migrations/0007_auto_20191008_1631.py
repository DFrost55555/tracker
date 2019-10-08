# Generated by Django 2.1.10 on 2019-10-08 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
        ('customers', '0005_customercontact_custcontact_role'),
        ('lists', '0003_listpriority_poitemtype_ragstatus_raidstatus_raidtype'),
        ('projects', '0006_auto_20191007_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectresources',
            name='pr_chargeunit_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.ChargeUnitType', verbose_name='charge unit'),
        ),
        migrations.AddField(
            model_name='projectresources',
            name='pr_customer_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Customer', verbose_name='customer'),
        ),
        migrations.AddField(
            model_name='projectresources',
            name='pr_location_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.Location', verbose_name='location'),
        ),
        migrations.AddField(
            model_name='projectresources',
            name='pr_supplier_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.Supplier', verbose_name='supplier'),
        ),
        migrations.AlterField(
            model_name='projectresources',
            name='pr_statustype_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.ResourceStatus', verbose_name='resource status'),
        ),
    ]