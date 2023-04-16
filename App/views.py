from django.shortcuts import render
from App import models
from .models import Food
import operator


def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = {}
    context["text"] = "фруктовый ввод..."

    return render(request, "index.html", context)


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


def statistics(request):
    """
        Отображение страницы с едой отфильтрованной по её рейтингу

        :param request: объект с деталями запроса
        :type request: :class:django.http.HttpRequest
        :return: объект ответа сервера с HTML-кодом внутри
        :rtype: :class:django.http.HttpResponse
    """
    context = dict()

    rating = models.Like.objects.all()
    rating_dict = dict()

    for item in rating:
        if item.fruit in rating_dict.keys():
            rating_dict[item.fruit] += 1
        else:
            rating_dict[item.fruit] = 1

    rating_list = list()

    for item in rating_dict:
        rating_list.append([item, rating_dict[item]])

    context['list'] = sorted(rating_list, key=operator.itemgetter(1))[::-1]
    return render(request, 'food_statistics.html', context)
