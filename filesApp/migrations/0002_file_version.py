# Generated by Django 4.1.7 on 2023-11-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='version',
            field=models.CharField(default='A1', max_length=20),
        ),
    ]