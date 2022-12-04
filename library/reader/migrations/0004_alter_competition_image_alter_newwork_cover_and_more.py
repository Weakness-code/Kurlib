# Generated by Django 4.1.2 on 2022-12-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_alter_competition_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.ImageField(upload_to='competition/', verbose_name='Изображение для конкурса'),
        ),
        migrations.AlterField(
            model_name='newwork',
            name='cover',
            field=models.ImageField(upload_to='works/', verbose_name='Обложка работы'),
        ),
        migrations.AlterField(
            model_name='virtualcard',
            name='cover',
            field=models.ImageField(upload_to='books/', verbose_name='Обложка'),
        ),
    ]
