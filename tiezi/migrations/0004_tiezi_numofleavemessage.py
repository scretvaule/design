# Generated by Django 3.2.5 on 2022-03-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiezi', '0003_auto_20220319_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiezi',
            name='numofleavemessage',
            field=models.IntegerField(default=0),
        ),
    ]
