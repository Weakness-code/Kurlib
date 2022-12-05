# Generated by Django 4.1.2 on 2022-12-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localhistory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localhistorymodel',
            name='album',
        ),
        migrations.RemoveField(
            model_name='localhistorymodel',
            name='image',
        ),
        migrations.AddField(
            model_name='localhistorymodel',
            name='images',
            field=models.ImageField(blank=True, upload_to='localhistory/'),
        ),
        migrations.DeleteModel(
            name='ImageAlbum',
        ),
    ]
