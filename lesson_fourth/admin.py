from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Example)  # Зарегистр. нашу модель

admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)
admin.site.register(models.Publication)
admin.site.register(models.Article)


# Переопределяем отображение админ. части для модели Author
class AuthorAdmin(admin.ModelAdmin):
	# list_display = ['name', 'surname']
	list_display = [field.name for field in models.Author._meta.fields]
	# exclude = ["name"] # прячет поле
	fields = ['name', 'surname'] # показывает только 2-ва поля, без даты
	list_filter = ['name']
	#search_fields = ['name', 'surname']  # Поиск по заданным полям
	search_fields = [field.name for field in models.Author._meta.fields] # Поиск по всем полям	
	class Meta:
		model = models.Author


admin.site.register(models.Author, AuthorAdmin)