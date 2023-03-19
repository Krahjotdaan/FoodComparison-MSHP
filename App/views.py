from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from App.forms import FruitCreationForm
from App import models


def index(request):
    """
    :param request: объект с деталями запроса
    :return: объект ответа сервера с HTML-кодом внутри
    """
    context = dict()
    context["text"] = "фруктовый ввод..."
    return render(request, "index.html", context)


@login_required
def food_creation(request):
    context = dict()
    if request.method == 'POST':
        form = FruitCreationForm(request.POST)

        if form.is_valid() is True:
            name = form.data['title']
            description = form.data['description']
            calories = form.data['calories']
            vitamins = form.data['vitamins']
            deahtdoze = form.data['death_doze']
            interesting_facts = form.data['interesting_fact']
            image = form.data['image']

            fruit = models.Food(name=name, author=request.user, searched=0,
                                description=description, deahtdoze=deahtdoze, calories=calories,
                                image=image)
            fruit.save()

            models.VitaminFood.objects.create(vitamin=vitamins, food=fruit)
            models.Fact.objects.create(food=fruit, description=interesting_facts)
    else:
        form = FruitCreationForm()
        context['form'] = form

    return render(request, 'food_creation.html', context=context)
