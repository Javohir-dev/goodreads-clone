# Generated by Django 4.0 on 2023-08-04 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookreview',
            old_name='start_given',
            new_name='stars_given',
        ),
    ]