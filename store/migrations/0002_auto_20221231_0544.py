# Generated by Django 3.1.13 on 2022-12-31 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storebill',
            name='fabric_color',
        ),
        migrations.AddField(
            model_name='storeitem',
            name='fabric_color',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
