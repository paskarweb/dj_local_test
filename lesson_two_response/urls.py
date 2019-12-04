from django.urls import path, re_path, include   
from . import views   

urlpatterns = [
    
    # re_path - использование регулярных выражений
    # r'^' - регулярное выражение начало строки       
    # r'^$' - пустая строка в url, пеоеходи в ф-цию home()
    #---old version django:  urls(r'^$', views.home),  #localhost:7600
    # path('items', views.items, name = "items"),  #localhost:7600/items

    re_path('^$', views.hello_response),  # http://localhost:7600/lessons-two-response
    re_path('redirect/$', views.http_redirect), # http://localhost:7600/lessons-two-response/redirect
    re_path('fun1/$', views.fun1), 
    re_path('render-html/$', views.render_html), # http://localhost:7600/lessons-two-response/render-html
    re_path('render-template/$', views.render_template), # http://localhost:7600/lessons-two-response/render-template
    re_path('render-to-response/$', views.func_render_to_response), # http://localhost:7600/lessons-two-response/render-to_response
    re_path('render-template/form-hendler/$',  views.form_hendler),
]
