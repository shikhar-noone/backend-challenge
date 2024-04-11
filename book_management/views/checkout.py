# -*- coding: utf-8 -*-
from email import message
from rest_framework.views import APIView
from book_management.models.checkout import CheckoutProduct
from book_management.models.member import Member
from book_management.models.book import Book
from django.http import HttpResponseBadRequest 
from django.db.models import Sum
from rest_framework.response import Response
from book_management.models.return_product import ReturnProduct
from book_management.serializers.checkout import CheckoutSerializer
from django.db import transaction 


class CheckoutView(APIView):
    def get(self, request, member_id):
        member = Member.objects.get(id=member_id)
        checkout_items = member.member_checkouts.all()
        ser = CheckoutSerializer(checkout_items, many=True)
        response_data = {"status": "success", "data": ser.data}
        return Response(data=response_data, status=200)


    def post(self, request, member_id):

        payload = request.data.copy()
        member = Member.objects.get(id=member_id)
        checkout_list = payload.get("checkout_list")
        with transaction.atomic():
            for checkout_product in checkout_list:
                book_id = checkout_product.get("book_id")
                number_of_copies = checkout_product.get("number_of_copies")
                book: Book = Book.objects.filter(id=book_id).last()
                if not book:
                    return HttpResponseBadRequest(data="Book id invalid.")
                checkout_book = book.book_checkouts.filter(member=member, is_active=True).last()
                # returned_book = book.book_returns.filter(member=member, is_active=True).last()
                returned_book = ReturnProduct.objects.filter(book=book, member=member).last()
                number_of_book_left = book.copies - (checkout_book.copies if checkout_book else 0) + (returned_book.copies if returned_book else 0)
                if number_of_copies > number_of_book_left:
                    return HttpResponseBadRequest(content=f"{book.name} is out of stock. Please try reserving.")
                if checkout_book:
                    checkout_book.copies += number_of_copies
                    checkout_book.save()
                else:
                    CheckoutProduct.objects.create(member=member, book=book, copies=number_of_copies)
            
        response_data = {"status": "success"}
        return Response(data=response_data, status=200)
