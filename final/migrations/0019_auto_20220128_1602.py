# Generated by Django 3.1.5 on 2022-01-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0018_r'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
