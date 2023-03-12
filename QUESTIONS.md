## Как на своей ветке обновить проект?
### git merge main

## Как открыть "умный" merge, для решения конфликтов?
### Git -> resolve conflicts

## Что делать после клонирования проекта
### переключиться на свою ветку
### прописать в консоль:
1) pip install -r requirements.txt
2) python3/python manage.py migrate

## Если вы создали ветку, а на сервере её нет
``` python
git push --set-upstream origin имя_ветки
```

## Если на сервере есть ветка, которой у вас нет
``` python
git cheсkout --track origin/имя_ветки
```

## Если нужно удалить ветку, которая находится на сервере
``` python
git push origin --delete имя_ветки
```

## Удаление локальных веток, уже удалённых на сервере
``` python
git remote prune origin
```
*** 