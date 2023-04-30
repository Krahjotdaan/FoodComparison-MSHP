from django.contrib import admin
import App.models as model

# Register your models here.
admin.site.register(model.Food)
admin.site.register(model.VitaminFood)
admin.site.register(model.Like)
