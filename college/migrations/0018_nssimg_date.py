# Generated by Django 2.2.12 on 2020-05-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0017_auto_20200523_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='nssimg',
            name='date',
            field=models.DateField(default=''),
        ),
    ]