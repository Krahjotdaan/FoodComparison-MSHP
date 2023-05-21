# Generated by Django 4.1.4 on 2023-05-17 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.IntegerField(default=0)),
                ('searched', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
                ('interesting_fact', models.CharField(default='ЕСЛИ ВИДИШЬ ЭТУ НАДПИСЬ, ТО ДОБАВЬ ИНТЕРЕСНЫЙ ФАКТ', max_length=1000)),
                ('deathdoze', models.IntegerField(default=1)),
                ('image', models.ImageField(default='https://goo.su/swyUm5', upload_to='media/')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vitamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fruit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='vitamins',
            field=models.ManyToManyField(to='App.vitamin'),
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('food', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.food')),
            ],
        ),
        migrations.CreateModel(
            name='Comprasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fruit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.food')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fruit_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.food')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]