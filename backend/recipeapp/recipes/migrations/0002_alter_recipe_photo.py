# Generated by Django 4.2.3 on 2023-07-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='', verbose_name='Фото'),
        ),
    ]
