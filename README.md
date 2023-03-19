
# Основные правила

- **ВСЕ задачи выдаются через GitLab (вкладка Issues), запросы на слияние своей ветки с веткой main тоже в GitLab (вкладка Merge requests)**
- За невыполнение срока, указанного в GitLab -1 балл (при условии, что вы доделали таск после срока на этой неделе);
- Если вы не отписали, что болеете или не успеваете, то ставится 2;
- Спорные моменты мы всегда можем решить;
- Следовать код стайлу (файл README);
- Коммиты пишутся по определённой структуре (файл README);
- Таски выдаются по новой каждую неделю.
- При начале работы со своей веткой прописываем git merge main КАЖДЫЙ РАЗ (т.к. изменённый main может повлиять напрямую на решение вашего таска);
- Если возникли конфликты то Git -> resolve conflicts;

***

# DOCS

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

## Самое главное: соблюдать CRUD (create, read, update, delete) для таблиц


## Variables (переменные)
#### Не делать:
``` python
x = 0 # неясно что значит
X = 0 # нет, просто нет
cnt = 0 # здесь лучше будет написать count = 0
```
#### Вот так можно
``` python
count = 0
i = 0 # только в цикле

```
 ---
## Functions names (имена функций)

#### НЕ ДЕЛАТЬ:

``` python
def sdfldfslksdflkjsdfalkj(): # просто не надо 
    pass

def pls_work(): # непонятная запись, неясно что она делает
    pass

def damag(): # грамматическая ошибка
    pass

def damageToPacman: # camelcase, в питоне пишем через нижнее подчеркивание
    pass
```
#### Вот так можно:
``` python
def damage_to_pacman:
    pass
```

---
## Classes (классы)
#### Не делать:
``` python
class Ldsfkjajlkdfs: # неясно, кто это
    pass
class pacman: # с маленькой буквы
    pass
```
#### Вот так можно:
``` python
class Pacman:
    pass
```
---

## Мотивационная цитата Игоря
>Быстро и легко можно получить только при***лей, для остального наберись терпения  
c. Игорь

> P.S. Код и коммиты пишутся СТРОГО по структуре, пердставленной выше
> 
> За несоблюдение может быть снижена оценка















