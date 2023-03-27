
# Основные правила

- **ВСЕ задачи выдаются через GitLab (вкладка Issues), запросы на слияние своей ветки с веткой staging тоже в GitLab (вкладка Merge requests)**
- За невыполнение срока, указанного в GitLab -1 балл (при условии, что вы доделали таск после срока на этой неделе);
- Если вы не отписали, что болеете или не успеваете, то ставится 2;
- Спорные моменты мы всегда можем решить;
- Следовать код стайлу (файл README);
- Коммиты пишутся по определённой структуре (файл README);
- Таски выдаются по новой каждую неделю.
- При начале работы со своей веткой прописываем git merge main КАЖДЫЙ РАЗ (т.к. изменённый main может повлиять напрямую на решение вашего таска);
- Если возникли конфликты то Git -> resolve conflicts;


***


# COMMITS

### git commit -m "type: что сделали на анг." -m "description"

*Type может быть следующим:*

- feat: (создана новая функция с изменениями)
- fix: (исправление ошибки)
- docs: (изменения в документации, например, изменение файла README)
- style: (форматирование, добавление пробела, табуляции, отсутствующие точки с запятой и т. д .;)
- refactor: (переработанный код, который не исправляет ошибку и не добавляет функцию)
- test: (добавление недостающих тестов, рефакторинг тестов; без изменения производственного кода)
- chore: (обновление рутинных задач и т. д.; без изменения производственного кода)
- pref: (улучшение производительности)
- build: (измения влияющие на итоговую сборку, системные или внешние зависимости) 


### Это будут выглядеть так:

``` python
git commit -m "build: Added scenes" -m "Я добвил сцену с игрой 
(game_scene.py), в неё можно добавить код инициализации призраков 
и пакмана"
```


***


# Code Style

## 1. DOCS

*Doc's NAME*

- param, parameter, arg, argument, key, keyword: описание параметра
- type: тип параметра + ссылка
- raises, raise, except, exception: указать где и когда взникает конкретное исключение
- var, ivar, cvar: описание переменной
- vartype: тип переменной + ссылка
- returns, return: описание возвращаемого значения 
- rtype: тип возвращаемого значения + ссылка
- meta: метаданные описания объекта (доступ к классу / объекту / функции)

*Например:*

```python
def get_snippet_page(request, ID):
    """
    Отображение главной страницы сайта
    
    :param request: объект с деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :param id: primary key в модели :class:`main.viwes.Shippet`
    :type id: int
    :return: объект ответа сервера с HTML-кодом внутри
    :rtype: :class:`django.http.HttpResponse`
    :raises: :class:`django.http.Http404` в случае, если сниппет с указынным ID не существует
    :meta public:
    """
    context = get_base_context(request, "Просмотр сниппета")
    try:
        record = Snippet.objects.get(id = id)
        context['addform'] = AddSnippetForm(
            initial = {
                'user': 'AnonymousUser',
                'name': record.name,
                'code': record.code,
            }
        )
    except Snippet.DoesNotExist:
        raise Http404
    return render(request, 'pages/view_snippet.html', context)
```


***


## 2. Соблюдаем CRUD для таблиц (create, read, update, delete)


***


## 3. Classes, Functions, Variables.

### 3.1 Variables (переменные)

``` python
count = 0
i = 0 # только в цикле
```

### 3.2 Functions names (имена функций)

``` python
def damage_to_pacman:
    pass
```

### 3.3 Classes (классы)

``` python
class Pacman:
    pass
```


***


> P.S. Код и коммиты пишутся СТРОГО по структуре, пердставленной выше
> 
> За несоблюдение может быть снижена оценка


***


## Мотивационная цитата
> Иногда лучше остаться спать дома в понедельник, чем провести всю неделю в отладке написанного в понедельник кода.  
















