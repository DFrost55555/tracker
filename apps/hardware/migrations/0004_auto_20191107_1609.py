# Generated by Django 2.1.10 on 2019-11-07 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0003_auto_20191107_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='hw_createdby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_cust_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Customer'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_ees1_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_ees2_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_ees3_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_ems_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_eol_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_eow_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_ext_code',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='External Part Code'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_hwcat_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.HardwareCategory'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_hwsts_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.HardwareStatus'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_int_code',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Internal Part Code'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_int_reference',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Internal Reference'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_modifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hw_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_plp_txt',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Product Lifecycle Policy'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_portsts_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.PortfolioStatus'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_repl_desc',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Replacement Hardware Description'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_repl_vend_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hw_repl_vend_id', to='vendors.Vendor'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_see_txt',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Support End Estimated'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_upd_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hw_vend_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendor'),
        ),
        migrations.AlterField(
            model_name='hardwarecontact',
            name='hwcontact_email',
            field=models.EmailField(blank=True, max_length=250, null=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='hardwarecontact',
            name='hwcontact_firstname',
            field=models.CharField(max_length=150, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='hardwarecontact',
            name='hwcontact_lastname',
            field=models.CharField(max_length=150, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='hardwarecontact',
            name='hwcontact_mobnumber',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='hardwarecontact',
            name='hwcontact_role',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='hardwarecontact',
            name='hwcontact_telnum',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Telephone Number'),
        ),
    ]
