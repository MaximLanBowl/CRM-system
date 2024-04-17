# Generated by Django 5.0.4 on 2024-04-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='Почта: Email', max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default='Номер телефона: ', max_length=15),
        ),
    ]
