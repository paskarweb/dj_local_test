from django.urls import path
from . import views   # . текущий каталог/дириктория

urlpatterns = [

    path('', views.show),
]
