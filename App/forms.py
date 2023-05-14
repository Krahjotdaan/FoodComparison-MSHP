from django import forms


class FruitCreationForm(forms.Form):

    V_CHOICES = (
        ("A1", "A1"), ("A2", "A2"), ("B1", "B1"), ("B2", "B2"),
        ("B3", "B3"), ("B5", "B5"), ("B6", "B6"), 
        ("B7", "B7"), ("B9", "B9"), ("B12", "B12"), 
        ("C", "C"), ("D", "D"), ("Е", "Е"), ("K1", "K1"), ("K2", "K2"))

    image = forms.ImageField(widget=forms.FileInput(attrs={"id": "image_field"}))

    title = forms.CharField(label='Название',
                            max_length=25,
                            required=True,
                            widget=forms.TextInput(attrs={"placeholder": "Название..", "id": "title_field"}))

    description = forms.CharField(label='Описание',
                                  max_length=255,
                                  required=True,
                                  widget=forms.Textarea(attrs={"placeholder": "Описание..", "id": "description_field"}))

    calories = forms.IntegerField(label='Калории(на 1 кг)', 
                                  max_value=1000, 
                                  required=True,
                                  widget=forms.NumberInput(attrs={"id": "calories"}))

    vitamins = forms.MultipleChoiceField(label='Витамины (мг)',
                            required=True,
                            choices=V_CHOICES,
                            widget=forms.CheckboxSelectMultiple(attrs={"id": "choice_field"}))
    
    deathdoze = forms.IntegerField(label='Смертельная доза (кг)',
                                    max_value=1000000000, widget=forms.NumberInput(attrs={"id": "deathdoze"}))

    interesting_fact = forms.CharField(label='Интересный факт',
                                       max_length=255,
                                       widget=forms.Textarea(attrs={"placeholder": "Интересный факт..",
                                                                    "id": "interesting_fact_field"}))