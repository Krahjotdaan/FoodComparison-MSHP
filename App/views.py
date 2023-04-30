from django.shortcuts import render
from App import models
from random import randint
from .models import Food
from App import values_data
import operator


def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = {}
    data_guest= values_data.data_guest
    data_loged = values_data.data_loged
    indg = randint(0, len(data_guest) - 1)
    indl = randint(0, len(data_loged) - 1)
    context["index_g"] = data_guest[indg]
    context["index_l"] = data_loged[indl]
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
    food_id = request.GET['id']
    food = models.Food.objects.get(id=food_id)
    if 'id' in request.GET:
        context = {
            'food': food,
        }
    else:
        context = {
            'food': 'Ошибка',
        }

    if request.POST.get('like'):
        models.Like.objects.update_or_create(
            fruit=food,
            author=request.user
        )
    if request.POST.get('delete_like'):
        models.Like.objects.get(
            fruit=food,
            author=request.user
        ).delete()

    return render(request, "food_item.html", context)


def profile_page(request):
    return render(request, 'profile/page.html')


def like_page(request):
    context = dict()
    liked = models.Like.objects.all()
    context['liked'] = liked

    return render(request, 'like_page.html', context)


def statistics(request):
    """
        Отображение страницы с едой отфильтрованной по её рейтингу (в том числе и еда, не имеющая рейтинга)

        :param request: объект с деталями запроса
        :type request: :class:django.http.HttpRequest
        :return: объект ответа сервера с HTML-кодом внутри
        :rtype: :class:django.http.HttpResponse
    """

    context = dict()
    rating_dict = dict()
    rating_list = list()

    rating = models.Like.objects.all()
    food = models.Food.objects.all()

    for item in rating:
        if item.fruit in rating_dict.keys():
            rating_dict[item.fruit] += 1
        else:
            rating_dict[item.fruit] = 1

    for item in food:
        if item not in rating_dict.keys():
            rating_dict[item] = 0

    for item in rating_dict:
        rating_list.append([item, rating_dict[item]])

    context = {
        'list': sorted(rating_list, key=operator.itemgetter(1))[::-1]
    }

    return render(request, 'food_statistics.html', context)
