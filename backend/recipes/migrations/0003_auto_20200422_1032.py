# Generated by Django 3.0.5 on 2020-04-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20200422_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
