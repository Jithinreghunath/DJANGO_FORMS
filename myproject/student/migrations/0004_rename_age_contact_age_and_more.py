# Generated by Django 4.1.3 on 2022-11-14 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_contact_age_alter_contact_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='Descriptions',
        ),
    ]