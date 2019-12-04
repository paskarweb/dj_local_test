from django.urls import path, re_path   
from . import views   

urlpatterns = [
    
    # re_path - использование регулярных выражений
    # r'^' - регулярное выражение начало строки       
    # r'^$' - пустая строка в url, пеоеходи в ф-цию home()
    #---old version django:  urls(r'^$', views.home),  #localhost:7600
    path('items', views.items, name = "items"),  #localhost:7600/items
    path('items/2017/', views.special_case_2017, name = "special_case_2017"),  #localhost:7600/items/2017/
    re_path('^items/([0-9]{4,5})/$', views.year_archive, name = "year_archive"),  #localhost:7600/items/1234/
    re_path('^items/([0-9]{4})/([0-9]{2})/$', views.month_archive, name = "month_archive"),  #localhost:7600/items/2017/10
    re_path('^items/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})/$', views.day_archive, name = "day_archive"),  #localhost:7600/items/2019/10/16
    re_path('book/$', views.page, name = "page"),
    re_path('book/page(?P<num>[0-9]+)/$', views.page, name = "page"),
    path('', views.home),  #localhost:7600
    
]
