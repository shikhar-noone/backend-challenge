from rest_framework import serializers
from book_management.models.book import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
