# Generated by Django 3.1.1 on 2022-08-25 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_checkedcontent_checked_contents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkedcontent',
            old_name='checked_contents',
            new_name='users',
        ),
    ]
