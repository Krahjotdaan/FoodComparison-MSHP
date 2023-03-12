from django.contrib.auth.models import User
from django.db import models


class Fruit:
    pass


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
