# Generated by Django 4.1.2 on 2022-12-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurlib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branches',
            options={'verbose_name': 'Филиал', 'verbose_name_plural': 'Филиалы'},
        ),
    ]