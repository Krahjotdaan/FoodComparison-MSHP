from django.shortcuts import render
from App import models
from random import randint
import json
import operator
from django.http import JsonResponse
from .models import Food
from googleapiclient.discovery import build
from App import values_data



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

    # TODO: сделать на 42 строчке файла рабочий фон для витаминов
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
    if request.POST.get('delete_like'):
        try:
            models.Like.objects.get(
                fruit=food,
                author=request.user
            ).delete()
        except:
            pass

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


def get_youtube_links(*, food_name):
    '''
    Функция получения ссылок на видео с ютуба о определенной еде

    :return: str
    '''
    try:
        with open('youtube_api_key.json','r') as data:
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
    context = {
        "id": request.GET.get("id", 0)
    }

    return render(request, "complaint_add.html", context)


def complaint_list(request):
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
        context['vitamins'].append(Food.get_vitamins_by_food(i))
    context['zip'] = zip(context['food'], context['vitamins'])
    return render(request, "comprasion_page.html", context)
