# Generated by Django 4.1.7 on 2023-03-28 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='fullname',
        ),
    ]
