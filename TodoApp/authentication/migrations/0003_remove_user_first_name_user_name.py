# Generated by Django 4.0.5 on 2022-07-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]
