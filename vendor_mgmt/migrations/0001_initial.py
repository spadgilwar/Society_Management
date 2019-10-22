# Generated by Django 2.2.3 on 2019-10-22 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendor_info',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=12)),
                ('website', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Vendor Email')),
                ('service', models.CharField(max_length=50)),
                ('helpline_no', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='vendor_invoices',
            fields=[
                ('v_invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_no', models.CharField(max_length=15)),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField(null=True)),
                ('service_from', models.DateField()),
                ('service_to', models.DateField()),
                ('charges', models.FloatField()),
                ('billing_month', models.CharField(max_length=12)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_mgmt.vendor_info')),
            ],
        ),
    ]
