# Generated by Django 4.1.4 on 2022-12-19 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='parent',
        ),
    ]
