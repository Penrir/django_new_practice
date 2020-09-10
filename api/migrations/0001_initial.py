# Generated by Django 2.2.16 on 2020-09-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('typeq', models.IntegerField()),
                ('author', models.IntegerField()),
                ('title', models.CharField(max_length=300)),
                ('content', models.CharField(max_length=1500)),
                ('reg_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'Board',
            },
        ),
    ]
