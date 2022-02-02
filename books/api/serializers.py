from django.forms import fields
from rest_framework import serializers
from books import models

class BooksSerialazer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'


