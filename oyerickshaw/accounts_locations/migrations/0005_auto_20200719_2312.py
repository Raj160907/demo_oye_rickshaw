# Generated by Django 2.2.14 on 2020-07-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_locations', '0004_userlocation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
