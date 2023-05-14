# Generated by Django 4.1.7 on 2023-04-30 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_food_deathdoze_alter_food_searched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitaminfood',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.food'),
        ),
        migrations.AlterField(
            model_name='vitaminfood',
            name='vitamin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.vitamin'),
        ),
    ]
