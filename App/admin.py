from django.contrib import admin
import App.models as model

# Register your models here.
admin.site.register(model.Food)
admin.site.register(model.Like)
admin.site.register(model.Vitamin)
admin.site.register(model.Comprasion)
admin.site.register(model.Comment)
