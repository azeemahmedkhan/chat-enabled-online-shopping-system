# Generated by Django 3.2 on 2021-04-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
    ]
