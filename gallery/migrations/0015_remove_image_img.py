# Generated by Django 3.1.11 on 2021-05-26 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20210526_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img',
        ),
    ]
