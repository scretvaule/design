# Generated by Django 3.2.5 on 2022-04-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leavemessage', '0007_leavemessage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavemessage',
            name='havelike',
            field=models.BooleanField(default=False),
        ),
    ]