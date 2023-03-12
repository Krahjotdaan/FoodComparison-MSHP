from django.db import models

# Create your models here.


class Fact(models.Model):
    # Таблица интересных фактов
    id = models.IntegerField()
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

