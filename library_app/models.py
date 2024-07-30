from django.db import models
from book_app.models import Book
from client_app.models import Client

# Create your models here.
class Rental(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)