from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import forms

# Create your views here.

def test_view(request):
	str1 = request.path  + '<br>'
	str1 += request.get_host() + '<br>' 
	str1 += request.get_full_path() + '<br>'
	str1 += "Защищено {}".format(request.is_secure())
	return HttpResponse('welcome to {}'.format(str1))

def search(request):
	if request.method == "GET":
		if 'q' in request.GET:
			return HttpResponse("Вы хотели найти {}".format(request.GET['q']))
		else:
			return HttpResponse("Вы отправили пустую форму")


def search_form(request):
	return render(request, 'search_form.html')


def file_input(request):
	name = request.POST['name']
	surname = request.POST['surname']
	birth = request.POST['birth']
	gender = request.POST['gender']
	some_file = open("some1.txt", "w")
	some_file.write("Имя: " + name + "\n")
	some_file.write("Фамилия: " + surname + "\n")
	some_file.write("birth: " + birth + "\n")
	some_file.write("Пол: " + gender + "\n")
	some_file.close()	
	return HttpResponse("Данные учрешно сохранены в файл some1.txt")


def form(request):
	form_for_author1 = forms.AuthorOneForm
	form_for_article = forms.ArticleForm
	form_contact = forms.ContactForm
	context = {
		'form_for_author1': form_for_author1,
		'form_for_article': form_for_article,
		'form_contact': form_contact
	}
	return render(request, 'form.html', context)

def author_add(request):
	form = forms.AuthorOneForm(request.POST)
	result = "Автор добавлен {}".format(request.path)
	if request.method == "POST":
		if form.is_valid():
			data = form.cleaned_data   # содержит все данные объекта
			form.save()
			#print(data['name'])   # console.log
			return HttpResponse("Автор добавлен {}".format(request.path))

def add_article(request):
	form = forms.ArticleForm(request.POST)	
	if request.method == "POST" and form.is_valid():
		data = form.cleaned_data   # содержит все данные объекта
		form.save()
		#print(data['title'])   # console.log
		return HttpResponse("Статья добавлена!")
