# Generated by Django 4.2.10 on 2024-03-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='fwefwf', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
