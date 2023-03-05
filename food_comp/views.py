from django.shortcuts import render
from food_comp import models

def index(request):
    context = dict()
    context["text"] = "фруктовый ввод..."
    return render(request, "index.html", context)


# Create your views here.
