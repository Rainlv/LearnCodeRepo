# Generated by Django 2.1 on 2020-03-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('removed', models.BooleanField(default=0)),
            ],
        ),
    ]
