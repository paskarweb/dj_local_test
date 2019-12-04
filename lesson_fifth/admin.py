from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Author1)  # Зарегистр. нашу модель
admin.site.register(models.Article)


