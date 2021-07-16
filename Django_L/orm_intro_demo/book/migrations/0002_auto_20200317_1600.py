# Generated by Django 2.1 on 2020-03-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
