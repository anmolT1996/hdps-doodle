# Generated by Django 2.2.5 on 2020-02-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdps', '0004_auto_20200223_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
