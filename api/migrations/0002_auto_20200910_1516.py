# Generated by Django 2.2.16 on 2020-09-10 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='typeq',
            new_name='type',
        ),
    ]
