# Generated by Django 2.1.10 on 2020-01-15 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purorders', '0007_auto_20200115_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_charge_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='PO Charge Value'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_cost_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='PO Cost Value'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_status_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='purorders.POStatus', verbose_name='PO Status'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_unit_charge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='PO Unit Charge'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_unit_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='PO UNit Cost'),
        ),
    ]
