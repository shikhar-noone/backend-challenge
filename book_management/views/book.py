# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from book_management.models.checkout import CheckoutProduct
from book_management.models.member import Member
from book_management.models.book import Book
from django.http import HttpResponseBadRequest 
from django.db.models import Sum
from rest_framework.response import Response
from book_management.serializers.book import BookSerializer
from book_management.serializers.checkout import CheckoutSerializer
from django.db import transaction 


class BookListView(APIView):
    def get(self, request):
        try:
            books = Book.objects.all()

            ser = BookSerializer(books, many=True)
            response_data = {"status": "success", "data": ser.data}
            return Response(data=response_data, status=200)
        except:
            return Response(data={"message":"Error occured"})


    