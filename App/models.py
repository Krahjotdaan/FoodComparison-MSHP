from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages

class Food(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    searched = models.IntegerField()
    description = models.CharField(max_length=1000)
    deathdoze = models.IntegerField()

class VitaminFood(models.Model):
    #Таблица витамина в еде
    vitamin = models.OneToOneField(to=Vitamin, on_delete=models.CASCADE)
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)


class Fact(models.Model):
    # Таблица интересных фактов
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)


class Vitamin(models.Model):
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


class Like(models.Model):
    fruit = models.ForeignKey(to=Fruit, default=1, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)

    @staticmethod
    def add(fruit, author):
        Like.objects.create(
            fruit=fruit,
            author=author
        )

    @staticmethod
    def get():
        return Like.objects.all()
