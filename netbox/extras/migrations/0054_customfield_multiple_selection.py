# Generated by Django 3.1.3 on 2020-12-14 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0053_rename_webhook_obj_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='multiple_selection',
            field=models.BooleanField(default=False),
        ),
    ]
