# Generated by Django 2.2.28 on 2022-11-01 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addresszfmmvptnka'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresszfmmvptnka',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
