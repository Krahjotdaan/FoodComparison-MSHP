import os, shutil
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from App.forms import FruitCreationForm
from App import models


def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = {}
    context["text"] = "фруктовый ввод..."

    return render(request, "index.html", context)


@login_required
def food_creation(request):
    context = dict()
    if request.method == 'POST':
        form = FruitCreationForm(request.POST, request.FILES)

        name = form.data['title']
        description = form.data['description']
        vitamins = form.data['vitamins']
        print(vitamins)
        deathdoze = form.data['deathdoze']
        interesting_fact = form.data['interesting_fact']
        image = form.files['image']
        calories = form.data['calories']
        
        fruit = models.Food(name=name, author=request.user, searched=0,
                                description=description, deathdoze=deathdoze,
                                image=image, calories=calories,
                                interesting_fact=interesting_fact)
        fruit.save()

        

    else:
        form = FruitCreationForm()
        context['form'] = form

    form = FruitCreationForm()
    context['form'] = form

    return render(request, 'food_creation.html', context=context)


def food_list_page(request):
    """
    Отображение страницы со всей едой

    :param request: объект с деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    :meta public:
    """
    context = {}
    search_query = request.GET.get('search_fruit', '')

    if search_query:
        food = models.Food.objects.filter(name__iregex=search_query)
        context['food'] = food
    else:
        food = models.Food.objects.all()
        context['food'] = food

    return render(request, "food_list.html", context)


def food_item_page(request):
    """
    Отображение страницы с элементом базы данных Food

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    :meta public:
    """

    if 'id' in request.GET:
        food_id = request.GET['id']
        food = models.Food.objects.get(id=food_id)
        context = {
            'food': food,
        }
    else:
        context = {
            'food': 'Ошибка',
        }
    return render(request, "food_item.html", context)


def profile_page(request):
    return render(request, 'profile/page.html')
