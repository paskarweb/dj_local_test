from django.db import models

# Create your models here.


class Example(models.Model):
	integer_field			= models.IntegerField()
	positive_field			= models.PositiveIntegerField()
	positive_small_field 	= models.PositiveSmallIntegerField()
	big_integer_field 		= models.BigIntegerField()
	float_field 			= models.FloatField()
	binary_field			= models.BinaryField()
	boolean_field			= models.BooleanField()
	char_field				= models.CharField(max_length=5)
	text_field				= models.TextField(max_length=20)
	date_field				= models.DateField(auto_now = False)
	date_time_field			= models.DateTimeField(auto_now_add = True)
	decimal_field			= models.DecimalField(max_digits = 8, decimal_places = 2)
	email					= models.EmailField()
	file_field				= models.FileField(upload_to = 'file')
	image_field				= models.ImageField(upload_to = 'images')


class Author(models.Model):
	name	= models.CharField(max_length=50, verbose_name = "Имя")
	surname = models.CharField(max_length=50, verbose_name = "Фамилия")
	date_birth = models.DateField(auto_now=False, verbose_name = "Дата рождения")

	def __str__(self):
		return "Имя: %s Фамилия : %s" % (self.name, self.surname)

	# для перевод в русской расклдке:
	class Meta:
		verbose_name = "Автор"
		verbose_name_plural = "Авторы"


class Book(models.Model):
	CHOISE_GENRE = (
		('comedy', 'Comedy'),
		('tragedy', 'Tragedy'),
		('drama', 'Drama'),
	)

	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1000)
	genre = models.CharField(max_length=50, choices=CHOISE_GENRE)

	def __str__(self):
		return self.title + ' ' + self.genre



class Place(models.Model):
	name = models.CharField(max_length=50)
	adress = models.CharField(max_length=100)

	def __str__(self):
		return self.name + " the place"

class Restaurant(models.Model):
	place = models.OneToOneField(Place, on_delete = models.CASCADE)
	service_not_dogs = models.BooleanField(default=False)
	service_pizza = models.BooleanField(default=False)

	def __str__(self):
		return self.place.name + " the restaurant " 

class Waiter(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def __str__(self):
		return "{0} the waiter at {1}".format(self.name, self.restaurant)




class Publication(models.Model):
	title = models.CharField(max_length=30)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title', )


class Article(models.Model):
	headline = models.CharField(max_length=100)
	publications = models.ManyToManyField(Publication)

	def __str__(self):
		return self.headline

	class Meta:
		ordering = ('headline', )
	
