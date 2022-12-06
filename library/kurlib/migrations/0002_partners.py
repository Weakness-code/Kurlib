# Generated by Django 4.1.2 on 2022-12-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurlib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='partners_ico/', verbose_name='Иконка')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
            },
        ),
    ]