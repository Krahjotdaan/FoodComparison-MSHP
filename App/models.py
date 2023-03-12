from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages


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


class Vitamin(models.Model):
    vitamin_id = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    @staticmethod
    def get():
        return Vitamin.objects.all()

    @staticmethod
    def add(self, vitamin_id, name):
        Vitamin.objects.create(
            vitamin_id=vitamin_id,
            name=name
        )
        messages.success(self.request, 'Name added')

class Food(models.Model):
    food_id = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    searched = models.IntegerField()
    description = models.CharField(max_length=1000)
    deathdoze = models.IntegerField()


