# Generated by Django 2.2.13 on 2020-07-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('dojo', '0037_auto_20200707_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='authorized_groups',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
    ]