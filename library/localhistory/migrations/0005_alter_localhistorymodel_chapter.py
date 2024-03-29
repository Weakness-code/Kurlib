# Generated by Django 4.1.2 on 2022-12-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localhistory', '0004_localhistorymodel_chapter_localhistorymodel_image_0_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localhistorymodel',
            name='chapter',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Курагинский район'), (2, 'Курагино'), (3, 'Села и поселки'), (4, 'Мемориальные доски'), (5, 'Курагинцы в годы ВОВ'), (6, 'Литературная карта'), (7, 'Культура. Искусство. Библиотечное дело'), (8, 'Имя в истории района')], verbose_name='Раздел'),
        ),
    ]
