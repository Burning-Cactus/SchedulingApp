# Generated by Django 2.2rc1 on 2019-04-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20190404_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='officePhone',
            field=models.CharField(default=5555555555, max_length=12),
            preserve_default=False,
        ),
    ]
