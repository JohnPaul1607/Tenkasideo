# Generated by Django 4.1.7 on 2023-03-04 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gapp', '0019_remove_employers_selection_registered_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_registration_database',
            name='Increment_ID',
        ),
        migrations.RemoveField(
            model_name='employer_access_database',
            name='Incrementing_ID',
        ),
        migrations.RemoveField(
            model_name='employers_selection',
            name='Incrementing_ID',
        ),
        migrations.RemoveField(
            model_name='eployers_table',
            name='Incrementing_ID',
        ),
    ]