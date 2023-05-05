from django.shortcuts import render
from App import models
from django.http import JsonResponse
from .models import Food


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

def add_comprasion(request):
    # fruit = models.Food.objects.filter(id=request.GET.get("id"))

    fruit = request.GET.get('id')
    if not models.Comprasion.get_by_user(request.user).__contains__(models.Food.objects.get(id=fruit)):
        models.Comprasion.add(models.Food.objects.get(id=fruit), author=request.user)
    
    context = {
        'data': fruit
    }
    return JsonResponse(context)

def comprasion_page(request): # на доработке
    context = dict()
    context['food'] = models.Comprasion.get_by_user(request.user)
    context['vitamins'] = []
    for i in context['food']:
        context['vitamins'].append(Food.get_by_food(i))
    context['zip'] = zip(context['food'], context['vitamins'])
    return render(request, "comprasion_page.html", context)