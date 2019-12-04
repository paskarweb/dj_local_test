from django.urls import path, re_path   
from . import views      # . текущий каталог/дириктория
from . import forms

urlpatterns = [

    path('', views.form),
    re_path(r'^test-view/$', views.test_view),  #localhost:7600/lesson-fifth/test-view,    
    re_path(r'^search-form/$', views.search_form),
    re_path(r'^file-input/$', views.file_input),
    re_path(r'^search/$', views.search),  #localhost:7600/lesson-fifth/search,
    re_path(r'^add-author/$', views.author_add),
    re_path(r'^add-article/$', views.add_article),

]
