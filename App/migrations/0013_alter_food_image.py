# Generated by Django 4.1.7 on 2023-05-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='https://goo.su/swyUm5', upload_to='../media/'),
        ),
    ]
