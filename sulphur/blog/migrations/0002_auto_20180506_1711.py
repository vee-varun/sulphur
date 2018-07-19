# Generated by Django 2.0.3 on 2018-05-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_picture',
        ),
        migrations.AlterField(
            model_name='category',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
