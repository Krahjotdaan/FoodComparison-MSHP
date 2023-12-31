## Как на своей ветке обновить проект?

``` python
git merge main
```

## Как запушить только последний коммит?

``` python
git cherry-pick ветка
# для тимлидов
git merge --squash ветка
```

## Что делать после клонирования проекта?

### переключись на СВОЮ ветку и пропиши в консоль:

``` python
git config --global user.name "your name and surname"
git config --global user.email "your account"
python3/python manage.py migrate
```

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

## Как открыть "умный" merge, для решения конфликтов?

### Git -> resolve conflicts


*** 


## Мотивационная цитата
> Большинство хороших программистов делают свою работу не потому, что ожидают оплаты или признания, а потому что получают удовольствие от программирования.