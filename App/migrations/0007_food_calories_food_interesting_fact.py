# Generated by Django 4.1.7 on 2023-05-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_merge_20230509_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='interesting_fact',
            field=models.CharField(default='ЕСЛИ ВИДИШЬ ЭТУ НАДПИСЬ, ТО ДОБАВЬ ИНТЕРЕСНЫЙ ФАКТ', max_length=1000),
        ),
    ]