from django.urls import path, re_path, include   
from . import views   

extra_patterns = [
    re_path('report/$', views.report),
    re_path('report/(?P<id>[0-9]+)/$', views.report),
]

urlpatterns = [
    
    # re_path - использование регулярных выражений
    # r'^' - регулярное выражение начало строки       
    # r'^$' - пустая строка в url, пеоеходи в ф-цию home()
    #---old version django:  urls(r'^$', views.home),  #localhost:7600
    # path('items', views.items, name = "items"),  #localhost:7600/items
  
    
    re_path('blog/(page-(\d+)/)?$', views.blog_articles),  # bad practice http://localhost:7600/lessons-two-part2/blog/page-2
    re_path('comments/(?:page-(?P<page_number>\d+)/)?$', views.comments), # GOOD http://localhost:7600/lessons-two-part2/comments/page-2
 #   re_path('optional-args/(?P<year>[0-9]{4})/$', views.optional_args, {'foor': 'bar'}),  # http://localhost:7600/lessons-two-part2/optional-args/2222
    re_path('extra/', include(extra_patterns)), # http://localhost:7600/lessons-two-part2/extra/report/
]
