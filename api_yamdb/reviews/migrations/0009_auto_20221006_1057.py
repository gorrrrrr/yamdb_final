# Generated by Django 2.2.16 on 2022-10-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20221006_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genretitle',
            name='genre',
        ),
        migrations.AddField(
            model_name='genretitle',
            name='genre',
            field=models.ManyToManyField(to='reviews.Genre'),
        ),
    ]