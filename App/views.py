from random import randint
import json
import operator

from django.contrib.auth.decorators import login_required
from googleapiclient.discovery import build
from django.http import JsonResponse
from .models import Food
from googleapiclient.discovery import build
from App import values_data, models
from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from App.forms import FruitCreationForm, commentinputforme
from django.contrib import messages

register = template.Library()


def index(request):
    """
    Отображение главной страницы

    :param request: объект с деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    context = {}
    data_guest = values_data.data_guest
    data_loged = values_data.data_loged
    indg = randint(0, len(data_guest) - 1)
    indl = randint(0, len(data_loged) - 1)
    context["index_g"] = data_guest[indg]
    context["index_l"] = data_loged[indl]

    return render(request, "index.html", context)


@login_required
def food_creation(request):
    """
    Отображение страницы с добавлением своей еды

    :param request: объект с деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    context = dict()
    if request.method == 'POST':
        form = FruitCreationForm(request.POST, request.FILES)

        name = form.data['title']
        description = form.data['description']
        vitamins = request.POST.getlist('vitamins')
        deathdoze = form.data['deathdoze']
        interesting_fact = form.data['interesting_fact']
        image = form.files['image']
        calories = form.data['calories']

        fruit = models.Food(name=name, author=request.user, searched=0,
                            description=description, deathdoze=deathdoze,
                            image=image, calories=calories,
                            interesting_fact=interesting_fact)
        fruit.save()

        for v in vitamins:
            fruit.vitamins.create(name=v)

        messages.success(request, 'Фрукт создан')

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
    """

    food_id = request.GET['id']
    food = models.Food.objects.get(id=food_id)
    vitamins = models.Food.get_vitamins_by_food(food)
    if 'id' in request.GET:
        context = {
            'food': food,
            'vitamins': vitamins,
            'video_links': get_youtube_links(food_name=food.name)
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
        messages.success(request, "Вы лайкнули фрукт")
    if request.POST.get('delete_like'):
        try:
            models.Like.objects.get(
                fruit=food,
                author=request.user
            ).delete()
            messages.info(request, "Лайк удалён")
        except:
            pass
    if request.POST.get('add_to_comprasion'):
        models.Comprasion.objects.update_or_create(
            fruit=food,
            author=request.user
        )
        messages.success(request, "Добавлено к сравнению")
    if request.POST.get('delete_from_comprasion'):
        try:
            models.Comprasion.objects.get(
                fruit=food,
                author=request.user
            ).delete()
            messages.info(request, "Удалено из сравнения")
        except:
            pass

    return render(request, "food_item.html", context)


def profile_page(request):
    """
    Отображение страницы профиля

    :param request: объект с деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    context = {}
    liked = models.Like.objects.filter(author=request.user)
    try:
        context['liked'] = [liked[len(liked) - 3], liked[len(liked) - 2], liked[len(liked) - 1]]
    except:
        context['liked'] = liked
    return render(request, 'profile/page.html', context)


def statistics(request):
    """
    Отображение страницы с едой отфильтрованной по её рейтингу
    (в том числе и еда, не имеющая рейтинга)

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    """

    context = {}
    rating_dict = {}
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


def get_youtube_links(*, food_name):
    """
    Функция получения ссылок на видео с ютуба о определенной еде

    :param food_name: название еды, по которой будет производится поиск
    :type food_name: str
    :return: cписок, в котором находится 3 ссылки
    :rtype: str
    """
    try:
        with open('youtube_api_key.json', 'r') as data:
            API_KEY = json.load(data)['api_key']

        youtube = build("youtube", "v3", developerKey=API_KEY)

        search_response = youtube.search().list(
            q=f"факты о {food_name}",
            type="video",
            part="id,snippet",
            maxResults=3,
            relevanceLanguage='ru',
            safeSearch='moderate',
            videoDefinition='high',
            videoEmbeddable='true',
        ).execute()

        video_urls = []
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                video_urls.append(f"https://www.youtube.com/embed/{search_result['id']['videoId']}")

        return video_urls
    except Exception as error:
        print(repr(error))
        return None


def complaint_add(request):
    """
    Отображение страницы подачи жалоб

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    """
    context = {
        "id": request.GET.get("id", 0)
    }

    return render(request, "complaint_add.html", context)


def complaint_list(request):
    """
    Отображение страницы со всеми жалобами

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    """
    context = {}
    if request.method == 'POST':
        fruit = models.Food.objects.filter(id=request.POST.get('id'))[0]
        author = request.user
        complaint = request.POST.get('btnradio')
        models.Complaint.add(author, complaint, fruit)

    all_complaints = models.Complaint.get_all()
    context['all_complaints'] = all_complaints

    return render(request, "complaint_list.html", context)


def add_comprasion(request):
    """
    Обработка AJAX запроса по добавлению еды в таблицу для сравнения

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    """

    fruit = request.GET.get('id')
    if not (models.Comprasion.get_by_user(request.user).__contains__(models.Food.objects.get(id=fruit))) and len(
            models.Comprasion.get_by_user(request.user)) < 4:
        models.Comprasion.add(models.Food.objects.get(id=fruit), author=request.user)

    context = {
        'data': fruit
    }
    return JsonResponse(context)


def comprasion_page(request):
    """
    Отображение страницы сравнения еды

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    """
    context = {}
    context['food'] = models.Comprasion.get_by_user(request.user)
    context['vitamins'] = []
    for i in context['food']:
        context['vitamins'].append(models.Food.get_vitamins_by_food(i))

    context['count_food'] = len(context['food'])

    context['zip'] = zip(context['food'], context['vitamins'])

    if request.POST.get('clear_comprasion'):
        comprasion_list = models.Comprasion.get_by_user(request.user)
        for food in comprasion_list:
            models.Comprasion.objects.get(fruit=food, author=request.user).delete()

        return redirect("/comprasion/page/")

    return render(request, "comprasion_page.html", context)


@login_required
def delete_user(request):
    """
    Обработка и отображение удаления профиля

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    """
    user = request.user
    user.delete()
    return render(request, 'profile/page_deleted.html')


def comments_page(request):
    """
    Отображение страницы добавления отзыва о сервисе

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:django.http.HttpResponse
    """
    context = {}
    if request.method == "POST":
        context['form'] = commentinputforme()
        f = commentinputforme(request.POST)
        if f.is_valid():
            obj = models.Comment(author=request.user, text=f.data['text'])
            obj.save()
    else:
        context['form'] = commentinputforme()
    comentdata = models.Comment.objects.all()
    context['comments'] = comentdata
    return render(request, 'comments.html', context)


def like_page(request):
    """
    Отображение страницы с понравившейся едой

    :param request: объект с деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    """
    context = {}
    liked = models.Like.objects.all()
    context['liked'] = liked

    return render(request, 'like_page.html', context)




def add_like(request):
    """
    Обработка AJAX запроса, который добавляет лайк определенному объекту еды

    :param request: объект с деталями запроса
    :type request: :class:django.http.HttpRequest
    :return: HTTP response that consumes data to be serialized to JSON
    :rtype: :class:`django.http.HttpResponse`
    """
    context = {
        'data': 'ok'
    }
    try:
        likes = models.Like.objects.filter(
            author=request.user,
            fruit=models.Food.objects.filter(id=request.GET.get('id'))[0]
        )[0]
    except Exception as error:
        context = {
            'data': str(repr(error))
        }
        like = models.Like.objects.create(
            fruit=models.Food.objects.filter(id=request.GET.get('id'))[0],
            author=request.user
        ).save()

    return JsonResponse(context)
