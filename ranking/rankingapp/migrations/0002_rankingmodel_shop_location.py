# Generated by Django 4.2.7 on 2024-01-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rankingmodel',
            name='shop_location',
            field=models.CharField(default='location', max_length=100),
            preserve_default=False,
        ),
    ]
