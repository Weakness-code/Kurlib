# Generated by Django 4.1.2 on 2022-12-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localhistory', '0003_remove_localhistorymodel_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='localhistorymodel',
            name='chapter',
            field=models.CharField(default=None, max_length=250, verbose_name='Раздел'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_0',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_1',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_2',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_3',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_4',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_5',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_6',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_7',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_8',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='image_9',
            field=models.ImageField(default=None, upload_to='localhistory/', verbose_name='Изображение'),
        ),
    ]