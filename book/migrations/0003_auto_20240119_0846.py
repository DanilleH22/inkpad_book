# Generated by Django 3.2.23 on 2024-01-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_createchapter_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbook',
            name='biography',
            field=models.TextField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='createbook',
            name='excerpt',
            field=models.TextField(max_length=300),
        ),
    ]
