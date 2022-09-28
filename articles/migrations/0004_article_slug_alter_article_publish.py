# Generated by Django 4.1.1 on 2022-09-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]
