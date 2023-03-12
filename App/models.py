from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages


# Create your models here.

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
