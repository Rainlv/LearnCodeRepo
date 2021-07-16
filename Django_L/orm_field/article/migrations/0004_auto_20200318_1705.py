# Generated by Django 2.1 on 2020-03-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creat_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='removed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='自动填充', max_length=100),
        ),
    ]