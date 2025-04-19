from django.urls import path
from .views import *
urlpatterns = [
    path('upload/', bulk_upload_words, name='upload Words in bulk'),
    path('search-word/', search_word, name='search word'),
]
