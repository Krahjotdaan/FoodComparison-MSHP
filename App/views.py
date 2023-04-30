from django.shortcuts import render
from App import models
from random import randint
from .models import Food
import json
from googleapiclient.discovery import build



def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = {}
    data_guest= ["Здарово, солнышко!", "Ну привет человек!", "Приветик!",
            "Привет! Хорошо выглядишь!", "Привет, посетитель!", "Какая встреча!",
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

    if 'id' in request.GET:
        food_id = request.GET['id']
        food = models.Food.objects.get(id=food_id)
        context = {
            'food': food,
            'video_urls': get_youtube_links(food_name=food.name)
        }
    else:
        context = {
            'food': 'Ошибка',
        }
    return render(request, "food_item.html", context)


def profile_page(request):
    return render(request, 'profile/page.html')


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

