from rest_framework import viewsets
from books.api import serializers
from books import models


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerialazer
    queryset = models.Books.objects.all()

