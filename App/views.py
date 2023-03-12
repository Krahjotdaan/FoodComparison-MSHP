from django.shortcuts import render
#from food_comp import models

def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = dict()
    context["text"] = "фруктовый ввод..."
    return render(request, "index.html", context)