# Generated by Django 4.1.1 on 2022-10-27 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentteachercourse',
            old_name='dates',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='documentteachercourse',
            name='name_of_course',
        ),
    ]
