# Generated by Django 3.1.5 on 2022-02-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0031_auto_20220220_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchautotry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=100)),
                ('l', models.CharField(max_length=100)),
            ],
        ),
    ]
