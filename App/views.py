from django.shortcuts import render
from App import models, forms
from .models import Food, Complaint


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


def complaint_list(request):
    context = {}

    if request.method == 'POST':
        author = request.user
        complaint = request.POST.get('btnradio')
        post_id = request.POST.get('id')

        print(str(author) + str(complaint) + str(post_id))
        new_complaint = models.Complaint.add(author=author, complaint=complaint, post_id=post_id)
        new_complaint.save()

    all_complaints = Complaint.get_all()
    not_checked_complaints = Complaint.get_not_checked()
    context['not_checked_complaints'] = not_checked_complaints
    context['all_complaints'] = all_complaints

    return render(request, "complaint_list.html", context)

def complaint_add(request):
    context = {}

    context['author'] = request.user

    # new_complaint = Complaint.add(author="io", complaint="НАРУШЕНИЕ!", post_id=0, is_checked=False)
    # new_complaint.save()

    # if request.method == 'POST':
    #     complaint = Complaint()
    #     Complaint.add()

    return render(request, "complaint_add.html", context)

