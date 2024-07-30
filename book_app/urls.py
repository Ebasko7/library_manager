from django.urls import path
from .views import All_books

#from .views import 

urlpatterns = [
    path('books/' , All_books.as_view(), name='all_books')
]