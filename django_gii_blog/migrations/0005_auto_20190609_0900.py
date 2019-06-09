# Generated by Django 2.2 on 2019-06-09 06:00

from django.db import migrations, models
import django_gii_blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_blog', '0004_auto_20190608_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='created',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AlterField(
            model_name='file',
            name='field',
            field=models.FileField(upload_to=django_gii_blog.models.upload_to),
        ),
    ]
