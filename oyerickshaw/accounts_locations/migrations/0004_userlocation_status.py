# Generated by Django 2.2.14 on 2020-07-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_locations', '0003_auto_20200719_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlocation',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
