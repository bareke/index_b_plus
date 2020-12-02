from django.urls import path

from .views import index
from .views import search_no_indexed
from .views import search_indexed
from .views import create_product


urlpatterns = [
    path('', index, name='index'),
    path('no-indexed/', search_no_indexed, name='search_no_indexed'),
    path('indexed/', search_indexed, name='search_indexed'),
    path('create/', create_product, name='create_product')
]
