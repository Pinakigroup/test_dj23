# Generated by Django 3.2.10 on 2023-05-21 04:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('category', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreBill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('buyer_name', models.CharField(max_length=64, null=True)),
                ('report', models.CharField(choices=[('', 'Select'), ('Invoice', 'Invoice'), ('DC', 'DC')], max_length=64, null=True)),
                ('report_no', models.CharField(blank=True, max_length=64, null=True)),
                ('report_date', models.DateField(default=django.utils.timezone.now)),
                ('po_no', models.CharField(blank=True, max_length=64, null=True)),
                ('lc', models.CharField(max_length=64, null=True)),
                ('style_no', models.CharField(blank=True, max_length=32, null=True)),
                ('file_no', models.CharField(blank=True, max_length=64, null=True)),
                ('lot_no', models.CharField(blank=True, max_length=64, null=True)),
                ('fabric_detail', models.TextField()),
                ('store_location', models.CharField(blank=True, max_length=64, null=True)),
                ('order_qty', models.IntegerField(default=0)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliername', to='supplier.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.IntegerField(default=0)),
                ('totalprice', models.IntegerField(default=0)),
                ('fabric_color', models.CharField(blank=True, max_length=64, null=True)),
                ('uom', models.CharField(choices=[('', 'Select'), ('kg', 'kg'), ('miter', 'miter'), ('yard', 'yard'), ('pcs', 'pcs'), ('pound', 'pound'), ('g', 'g'), ('gg', 'gg'), ('litre', 'litre'), ('dg', 'dg'), ('1000 pcs', '1000 pcs')], max_length=64, null=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storebillno', to='store.storebill')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='StoreBillDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eway', models.CharField(blank=True, max_length=50, null=True)),
                ('veh', models.CharField(blank=True, max_length=50, null=True)),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('po', models.CharField(blank=True, max_length=50, null=True)),
                ('cgst', models.CharField(blank=True, max_length=50, null=True)),
                ('sgst', models.CharField(blank=True, max_length=50, null=True)),
                ('igst', models.CharField(blank=True, max_length=50, null=True)),
                ('cess', models.CharField(blank=True, max_length=50, null=True)),
                ('tcs', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.CharField(blank=True, max_length=50, null=True)),
                ('billno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storedetailsbillno', to='store.storebill')),
            ],
        ),
    ]
