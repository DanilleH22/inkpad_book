# Generated by Django 3.2.23 on 2024-01-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20240119_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbook',
            name='excerpt',
            field=models.TextField(max_length=500),
        ),
    ]