# Generated by Django 2.2.4 on 2019-12-06 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191206_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='items',
            new_name='item',
        ),
    ]