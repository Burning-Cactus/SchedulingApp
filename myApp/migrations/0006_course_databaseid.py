# Generated by Django 2.2 on 2019-04-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_user_databaseid'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='databaseID',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
