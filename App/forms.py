from django import forms


class FruitCreationForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20, required=True)
    description = forms.CharField(label='Описание', max_length=40, required=True)
    calories = forms.IntegerField(label='Калории(на 1 кг)', max_value=1000, required=True)
    vitamins = forms.NullBooleanField(label='Витамины', required=True)
    death_doze = forms.IntegerField(label='Смертельная доза(кг)', max_value=1000000000, required=True)
    interesting_fact = forms.CharField(label='Интересный факт', max_length=150, required=True)
    image = forms.ImageField()
