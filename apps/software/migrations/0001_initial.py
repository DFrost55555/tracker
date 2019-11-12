# Generated by Django 2.1.10 on 2019-11-11 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0001_initial'),
        ('lists', '0005_producttype'),
        ('customers', '0005_customercontact_custcontact_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('sw_id', models.AutoField(primary_key=True, serialize=False)),
                ('sw_description', models.CharField(max_length=250, verbose_name='Software Description')),
                ('sw_repl_desc', models.CharField(blank=True, max_length=250, null=True, verbose_name='Replacement Software Description')),
                ('sw_int_code', models.CharField(blank=True, max_length=250, null=True, verbose_name='Internal Part Code')),
                ('sw_ext_code', models.CharField(blank=True, max_length=250, null=True, verbose_name='External Part Code')),
                ('sw_eol_date', models.DateField(blank=True, null=True, verbose_name='End of Life')),
                ('sw_eow_date', models.DateField(blank=True, null=True, verbose_name='End of Warranty')),
                ('sw_ems_date', models.DateField(blank=True, null=True, verbose_name='End of Mainstream Support')),
                ('sw_ees1_date', models.DateField(blank=True, null=True, verbose_name='End of Extended Support - Period One')),
                ('sw_ees2_date', models.DateField(blank=True, null=True, verbose_name='End of Extended Support - Period Two')),
                ('sw_ees3_date', models.DateField(blank=True, null=True, verbose_name='End of Extended Support - Period Three')),
                ('sw_see_txt', models.CharField(blank=True, max_length=250, null=True, verbose_name='Support End Estimated')),
                ('sw_plp_txt', models.CharField(blank=True, max_length=250, null=True, verbose_name='Product Lifecycle Policy')),
                ('sw_upd_date', models.DateField(blank=True, null=True, verbose_name='Info Update')),
                ('sw_int_reference', models.CharField(blank=True, max_length=250, null=True, verbose_name='Internal Reference')),
                ('sw_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('sw_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('sw_createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('sw_cust_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Customer', verbose_name='Customer')),
                ('sw_modifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sw_editor', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareContact',
            fields=[
                ('swcontact_id', models.AutoField(primary_key=True, serialize=False)),
                ('swcontact_firstname', models.CharField(max_length=150, null=True, verbose_name='First Name')),
                ('swcontact_lastname', models.CharField(max_length=150, null=True, verbose_name='Last Name')),
                ('swcontact_role', models.CharField(blank=True, max_length=150, null=True, verbose_name='Role')),
                ('swcontact_email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='Email Address')),
                ('swcontact_telnum', models.CharField(blank=True, max_length=150, null=True, verbose_name='Telephone Number')),
                ('swcontact_mobnumber', models.CharField(blank=True, max_length=150, null=True, verbose_name='Mobile Number')),
                ('swcontact_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swcontact_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swcontact_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swcontact_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swcontact_editor', to=settings.AUTH_USER_MODEL)),
                ('swcontact_sw_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='software.Software', verbose_name='Software')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareNote',
            fields=[
                ('swnote_id', models.AutoField(primary_key=True, serialize=False)),
                ('swnote_note', models.CharField(max_length=2500, verbose_name='Note')),
                ('swnote_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swnote_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swnote_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swnote_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swnote_editor', to=settings.AUTH_USER_MODEL)),
                ('swnote_sw_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='software.Software', verbose_name='Software')),
            ],
        ),
        migrations.CreateModel(
            name='SWPortfolioStatus',
            fields=[
                ('swportsts_id', models.AutoField(primary_key=True, serialize=False)),
                ('swportsts_name', models.CharField(max_length=150, verbose_name='SW Portfolio Status Name')),
                ('swportsts_createddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('swportsts_modifieddate', models.DateTimeField(auto_now=True, null=True)),
                ('swportsts_createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('swportsts_modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='swportsts_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='software',
            name='sw_portsts_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='software.SWPortfolioStatus', verbose_name='Portfolio Status'),
        ),
        migrations.AddField(
            model_name='software',
            name='sw_repl_vend_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sw_repl_vend_id', to='vendors.Vendor', verbose_name='Replacement Vendor'),
        ),
        migrations.AddField(
            model_name='software',
            name='sw_swcat_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.SoftwareCategory', verbose_name='Software Category'),
        ),
        migrations.AddField(
            model_name='software',
            name='sw_swsts_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.SoftwareStatus', verbose_name='Software Status'),
        ),
        migrations.AddField(
            model_name='software',
            name='sw_vend_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendor', verbose_name='Vendor'),
        ),
    ]