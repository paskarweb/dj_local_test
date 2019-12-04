from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def show(request):
    ls = [5, 2, 4, 4]
    lsort = [51, 2, 41, 4]
    lsort.sort()
    return HttpResponse("Hello Django World! {}; Length= {}; Sort= {} ".format(ls, len(ls), lsort))
