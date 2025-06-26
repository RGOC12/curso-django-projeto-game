from django.contrib import admin
from . import models
# Register your models here.
class CategoriAdmin(admin.ModelAdmin):
    ...

@admin.register(models.game)
class GamesAdmin(admin.ModelAdmin):
    ...

admin.site.register(models.categori,CategoriAdmin)