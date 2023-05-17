from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime


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
    calories = models.IntegerField(default=0)
    searched = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    interesting_fact = models.CharField(max_length=1000, default="ЕСЛИ ВИДИШЬ ЭТУ НАДПИСЬ, ТО ДОБАВЬ ИНТЕРЕСНЫЙ ФАКТ")
    deathdoze = models.IntegerField(default=1)
    vitamins = models.ManyToManyField(to=Vitamin)
    image = models.ImageField(upload_to='media/', default="https://goo.su/swyUm5")

    @staticmethod
    def add(name, author, calories, searched, description, interesting_fact, deathdoze, image):
        Food.objects.create(
            name=name,
            author=author,
            calories=calories,
            searched=searched,
            description=description,
            interesting_fact=interesting_fact,
            deathdoze=deathdoze,
            image=image
        )

    @staticmethod
    def get_vitamins_by_food(food):
        vitaminfood = food.vitamins.all()
        return vitaminfood
        


# class VitaminFood(models.Model):
#     """
#     Таблица отношения существующего витамина к определенной еде

#     :var food: Еда, в которой содержится витамин
#     :var vitamin: Ссылка на витамин, который есть в еде
#     """
#     vitamin = models.ForeignKey(to=Vitamin, on_delete=models.CASCADE)
#     food = models.ForeignKey(to=Food, on_delete=models.CASCADE)


#     @staticmethod
#     def add(vitamin, food):
#         VitaminFood.objects.create(
#             vitamin=vitamin,
#             food=food
#         )


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


class Comprasion(models.Model):
    fruit = models.ForeignKey(to=Food, default=1, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)

    def add(fruit, author):
        Comprasion.objects.create(fruit=fruit, author=author)

    def get_by_user(user): 
        """
        Возвращает всю еду, которая в списке сравнения пользователя
        """
        comprasions = list(Comprasion.objects.filter(author=user))
        result = []
        for i in comprasions:
            result.append(i.fruit)
        return result


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

# class VitaminFood(models.Model):
#     """
#     Таблица отношения существующего витамина к определенной еде
#     :var food: Еда, в которой содержится витамин
#     :var vitamin: Ссылка на витамин, который есть в еде
#     """
#     vitamin = models.ForeignKey(to=Vitamin, on_delete=models.CASCADE)
#     food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
#     @staticmethod
#     def add(vitamin, food):
#         VitaminFood.objects.create(
#             vitamin=vitamin,
#             food=food
#         )