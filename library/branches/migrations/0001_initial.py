# Generated by Django 4.1.2 on 2022-12-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название филиала')),
                ('weekend', models.CharField(max_length=250, verbose_name='Выходные дни')),
                ('manager', models.CharField(max_length=250, verbose_name='Заведующая')),
                ('lunch_break', models.CharField(max_length=250, verbose_name='Перерыв на обед')),
                ('working_hours', models.CharField(max_length=250, verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
    ]
