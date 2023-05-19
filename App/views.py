from django.shortcuts import render
from App import models
from random import randint
from .models import Food


def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = {}
    data_guest = ["Здарово, солнышко!", "Ну привет человек!",
                  "critical error ||| reload page ||| please", "Привет, дорогой!",
                  "Приветик!", "Привет! Хорошо выглядишь!", "Привет, посетитель!", "Какая встреча!",
                  "Ура ты снова тут!", "Рад тебя видеть!", "Заходи сюда почаще, мне это это нравится!"]
    data_loged = ["Здарово, ", "Ну привет, ", "Ты ли это, ", "Как дела, ", "Приветик, ",
                  "Михао, ", "Привет, ", "Теперь ты - ", "Хорошего тебе дня, ", "Приветствую тебя, ",
                  "Кого я вижу, это же ", "О, здравствуй, мой драгоценный, "]
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

    if 'breakfast' in request.POST:
        food_id = request.POST['breakfast']
        food = models.Food.objects.get(id=food_id)
        models.Breakfast.objects.update_or_create(
            breakfast=food,
            author=request.user
        )
    breakfast_food = models.Breakfast.objects.all()
    context['breakfast_food'] = breakfast_food

    if 'lunch' in request.POST:
        food_id = request.POST['lunch']
        food = models.Food.objects.get(id=food_id)
        models.Lunch.objects.update_or_create(
            lunch=food,
            author=request.user
        )
    lunch_food = models.Lunch.objects.all()
    context['lunch_food'] = lunch_food

    if 'dinner' in request.POST:
        food_id = request.POST['dinner']
        food = models.Food.objects.get(id=food_id)
        models.Dinner.objects.update_or_create(
            dinner=food,
            author=request.user
        )
    dinner_food = models.Dinner.objects.all()
    context['dinner_food'] = dinner_food

    try:
        food_id = request.POST['breakfast_delete']
        food = models.Food.objects.get(id=food_id)
        models.Breakfast.objects.get(
            breakfast=food,
            author=request.user
        ).delete()
    except:
        pass

    try:
        food_id = request.POST['lunch_delete']
        food = models.Food.objects.get(id=food_id)
        models.Lunch.objects.get(
            lunch=food,
            author=request.user
        ).delete()
    except:
        pass

    try:
        food_id = request.POST['dinner_delete']
        food = models.Food.objects.get(id=food_id)
        models.Dinner.objects.get(
            dinner=food,
            author=request.user
        ).delete()
    except:
        pass

    return render(request, 'like_page.html', context)
