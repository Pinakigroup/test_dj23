# Generated by Django 3.2.10 on 2023-05-21 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=124)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.stock')),
            ],
        ),
    ]
