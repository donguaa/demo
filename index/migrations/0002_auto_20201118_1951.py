# Generated by Django 3.1.3 on 2020-11-18 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type_id',
            new_name='type',
        ),
    ]
