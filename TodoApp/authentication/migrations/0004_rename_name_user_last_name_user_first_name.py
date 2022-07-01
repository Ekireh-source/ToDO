# Generated by Django 4.0.5 on 2022-07-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_first_name_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=True, max_length=240),
            preserve_default=False,
        ),
    ]