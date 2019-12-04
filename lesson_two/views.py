from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse("<h1>Home Page!</h1>")

def items(request):
	return HttpResponse("Welcome to localhost/items")

def special_case_2017(request):
	return HttpResponse("Welcome to localhost/items/2017")

def year_archive(request, a1):
	return HttpResponse("Welcome to localhost/items/<b>^items/([0-9]{4})/$</b>! <br> a1= %s" %a1)

def month_archive(request, year, month):
	return HttpResponse("Welcome to localhost/items/<b>^items/[0-9]{4}/[0-9]{2}$</b> <br> year= %s " %year)

def day_archive(request, year, month, day):
	return HttpResponse("Welcome to localhost/items/<b>^items/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})/$</b> <br> year= %s " %year)

def page(request, num = "1"):
	if num == "1":
		return HttpResponse("Вы перешли на первую страницу книги!")
	else:
		return HttpResponse("Вы перешли на страницу под номером %s" %num)