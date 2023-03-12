from django.db import models

class VitaminFood(models.Model):
    #Таблица витамина в еде
    id = models.IntegerField()
    vitamin = models.OneToOneField(to=Vitamin, on_delete=models.CASCADE)
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)

class Food(models.Model):
    food_id = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    searched = models.IntegerField()
    description = models.CharField(max_length=1000)
    deathdoze = models.IntegerField()


