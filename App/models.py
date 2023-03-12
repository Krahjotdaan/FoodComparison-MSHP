from django.db import models

class VitaminFood(models.Model):
    #Таблица витамина в еде
    id = models.IntegerField()
    vitamin = models.OneToOneField(to=Vitamin, on_delete=models.CASCADE)
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)


class Fact(models.Model):
    # Таблица интересных фактов
    id = models.IntegerField()
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

