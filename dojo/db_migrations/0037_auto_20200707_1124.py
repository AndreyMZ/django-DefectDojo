# Generated by Django 2.2.13 on 2020-07-07 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0036_system_settings_email_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endpoint',
            name='fqdn',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='port',
        ),
    ]