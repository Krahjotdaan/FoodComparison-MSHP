from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
class Food(models.Model):
    """
    Таблица еды

    :var name: Название еды
    :var author: Человек, создавший данный продукт на сайте
    :var searched: Сколько раз на фрукт нажимали, чтобы узнать информацию о нём
    :var description: Описание еды
    :var deathdoze: Количество еды, необходимое для смерти челока от нее
    """
    name = models.CharField(max_length=100)
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    searched = models.IntegerField()
    description = models.CharField(max_length=1000)
    deathdoze = models.IntegerField()

    @staticmethod
    def new_food(name, author, searched, description, deathdoze):
        Food.objects.create(
            name=name,
            author=author,
            searched=searched,
            description=description,
            deathdoze=deathdoze
        )


class Vitamin(models.Model):
    """
    Таблица существующего витамина

    :var name: Название витамина (A, B, C, D и так далее)
    """
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

class VitaminFood(models.Model):
    """
    Таблица отношения существующего витамина к определенной еде

    :var food: Еда, в которой содержится витамин
    :var vitamin: Ссылка на витамин, который есть в еде
    """
    vitamin = models.OneToOneField(to=Vitamin, on_delete=models.CASCADE)
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)

    @staticmethod
    def add(vitamin, food):
        VitaminFood.objects.create(
            vitamin=vitamin,
            food=food
        )

class Fact(models.Model):
    """
    Таблица интересного факта, относящегося к определенной еде

    :var food: Ссылка на еду
    :var description: Описание самого интересного факта
    """
    food = models.OneToOneField(to=Food, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    @staticmethod
    def add(description, food):
        Fact.objects.create(
            description=description,
            food=food
        )


class Like(models.Model):
    """
    Таблица лайка к определенной еде

    :var fruit: Ссылка на еду
    :var author: Человек, лайкнувший еду
    """
    fruit = models.ForeignKey(to=Food, default=1, on_delete=models.CASCADE)
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

class Comment(models.Model):
    """
    Таблица комментариев

    :name: подпись оставившего отзыв
    :date: дата , когда оставлен комменатрий
    :text: содержание комментраия

    """
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)
    #date = models.CharField()
    text = models.CharField(max_length=500)


    @staticmethod
    def get():
        return Comment.objects.all()