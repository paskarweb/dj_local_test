from django.shortcuts import render
import datetime , math
from django.http import HttpResponse
from django.template import loader  # подключяем метод loader, который рендерить страницу

# Create your views here.

#--- OLD practice ---
#def view_old(request):
#	list = [0,232,45,123,4,53423,54,23]
#	template = loader.get_template('index.html')
#	context = {
#		"test": "TEXT!",
#		"list": list,
#		"name": "Alex",
#		"surname": "Jazun",
#		"coords": {
#			"x": "x coords",
#			"y": "y coords",
#		},
#		# "list": [1,2,3,4]  #---переопределили массив
#	}
#	return HttpResponse(template.render(context, request))

def view(request):
	list = [0,232,45,123,4,53423,54,23]	
	context = {
		"test": "TEXT!",
		"list": list,
		"name": "Alex",
		"surname": "Jazun",
		"coords": {
			"x": "x coords",
			"y": "y coords",
		},
		# "list": [1,2,3,4]  #---переопределили массив
	}
	return render(request, "index.html", context)

def filter(request):
	array_for_sort = [

		{'name': 'zed', 'age': 19},
		{'name': 'amy', 'age': 22},
		{'name': 'joe', 'age': 31},
	]

	context = {

		"name_low": "LOWER",
		"value" : 10,
		"first" : [1,2,3,4],
		"second" : [5,6,7,8],
		"str": "I'm using Django",
		"date": datetime.datetime.now(),
		"empty_one": "",
		"for_sort": array_for_sort,
		"float": 32.2235,
		"number": 12345678,
		"boolean_var": True,
		"name": "alex"
	}

	return render(request, "filter.html", context)

def tags_if(request):
	list = [1,2,3,4,5,6]
	var1 = "var1"
	var2 = "var2"
	var3 = "var3"
	obj = {
		'name' : "Alex",
		'surname' : "Parker"
	}

	context = {
		"x" : "x value",
		"user" : "Admin",
		"list" : list,
		"value" : 10,
		"obj" : obj,
		"var" : "var1",		
	}
	return render(request, "tags_if.html", context)

def tags_for(request):
	list = [1, 2, 3, 4, 5, 6]
	empty = []
	context = {

		"list": list,
		"empty": empty,

	}
	return render(request, 'tags_for.html', context)

def tag_regroup(request):
	people = [
		{'first_name': 'George', 'Last_name': 'Bush', 'gender': 'Male'},
		{'first_name': 'Bill', 'Last_name': 'Clinton', 'gender': 'Male'},
		{'first_name': 'Margaret', 'Last_name': 'Tatcher', 'gender': 'Female'},
		{'first_name': 'Pat', 'Last_name': 'Smith', 'gender': 'Unknown'},
	]

	people_for_test = [
		{'first_name': 'Margaret', 'Last_name': 'Tatcher', 'gender': 'Female'},
		{'first_name': 'George', 'Last_name': 'Bush', 'gender': 'Male'},	
		{'first_name': 'Pat', 'Last_name': 'Smith', 'gender': 'Unknown'},
		{'first_name': 'Bill', 'Last_name': 'Clinton', 'gender': 'Male'},	
	]	

	context = {	
		"people": people,
		"people_for_test" : people_for_test,
	}
	return render(request, 'regroup.html', context)

def base(request):
	context = {}
	return render(request, 'base.html', context)

def adrian(request):
	context = {
		'name' : "Адриан",
		'surname' : 'Головатый',
	}
	return render(request, 'adrian.html', context)	

def realese(request):
	obj = (
		{'year': 2015, "version": "1.8"},
		{'year': 2016, "version": "1.9"},
		{'year': 2017, "version": "1.11"},
	)

	context = {
		'obj': obj,
	}

	return render(request, 'realese.html', context)		