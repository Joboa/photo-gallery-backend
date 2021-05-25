# Generated by Django 3.1.11 on 2021-05-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('F', 'flower'), ('E', 'engine'), ('R', 'roads'), ('C', 'calculus')], default='', max_length=50),
        ),
    ]