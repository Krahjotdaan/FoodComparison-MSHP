
from django.shortcuts import render
from App import models

def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = dict()
    context["text"] = "фруктовый ввод..."
    return render(request, "index.html", context)


def food_list_page(request):
    food = models.Food.objects.all()
    context = {
        'food': food,
    }
    return render(request, "food_list.html", context)