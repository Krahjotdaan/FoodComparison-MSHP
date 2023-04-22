from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages

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



class Complaint(models.Model):
    """

    """
    author = models.ForeignKey(to=User, default=0, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=1000)
    fruit_id = models.ForeignKey(to=Food, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'Пользователь {self.author} послал {self.complaint} на фрукт {self.fruit_id.name}\n'

    @staticmethod
    def add(author, complaint, fruit_id):
        Complaint.objects.create(
            author=author,
            complaint=complaint,
            fruit_id=fruit_id
        )

    @staticmethod
    def get_all():
        return Complaint.objects.all().order_by("-id")































# class Complaint(models.Model):
#
#     author = models.ForeignKey(to=User, default=0, on_delete=models.CASCADE)
#     complaint = models.CharField(max_length=1000)
#     post_id = models.ForeignKey(to=Food, default=0, on_delete=models.CASCADE)
#     post_id_id = models.IntegerField(default=0, null=False)
#     is_checked = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'Пользователь {self.author} послал {self.complaint} \n'
#                # f'на пост с id {self.post_id}'
#
#     @staticmethod
#     def add(author, complaint, post_id, is_checked):
#         Complaint.objects.create(
#             author=author,
#             complaint=complaint,
#             post_id=post_id,
#             is_checked=is_checked,
#         )
#
#     @staticmethod
#     def get_all():
#         return Complaint.objects.all()
#
#     @staticmethod
#     def get_not_checked():
#         return Complaint.objects.filter(is_checked=False)