# Generated by Django 2.2.1 on 2019-05-27 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='hire_date_date',
            new_name='hire_date',
        ),
    ]