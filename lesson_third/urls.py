from django.urls import path, re_path   
from . import views   

urlpatterns = [
    
    # re_path - использование регулярных выражений
    # r'^' - регулярное выражение начало строки       
    # r'^$' - пустая строка в url, пеоеходи в ф-цию home()
   
   path('view', views.view),  #localhost:7600/lessons-third/view  
   path('filters', views.filter),  #localhost:7600/lessons-third/filters
   path('tags-if', views.tags_if),  #localhost:7600/lessons-third/tags-if
   re_path(r'^tags-for/$', views.tags_for),  #localhost:7600/lessons-third/tags-for
   re_path(r'^regroup/$', views.tag_regroup),  #localhost:7600/lessons-third/regroup
   re_path(r'^base/$', views.base),  #localhost:7600/lessons-third/base
   re_path(r'^adrian/$', views.adrian),  #localhost:7600/lessons-third/adrian
   re_path(r'^realese/$', views.realese),  #localhost:7600/lessons-third/realese
 
    
]
