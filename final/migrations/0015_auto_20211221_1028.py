# Generated by Django 3.1.5 on 2021-12-21 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0014_auto_20211220_1303'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='ownerformfill',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]