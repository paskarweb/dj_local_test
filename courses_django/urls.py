"""courses_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path , include
#from lesson_two import views

urlpatterns = [
    
    # r'^' - регулярное выражение начало строки
    # path(r'', include('lesson_one.urls')),
    path('admin/', admin.site.urls),
    path('lessons-two-part2/', include('lesson_two_part2.urls')),
    path(r'', include('lesson_two.urls')),    
    path('lessons-two-response/', include('lesson_two_response.urls')),
    path('lessons-third/', include('lesson_third.urls')),
    path('lesson-fifth/', include('lesson_fifth.urls')),
    # path(r'', views.home),  #localhost:7600
]
