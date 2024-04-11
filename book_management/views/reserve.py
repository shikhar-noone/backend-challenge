# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from book_management.models.member import Member
from book_management.models.book import Book
from django.http import HttpResponseBadRequest 
from rest_framework.response import Response
from book_management.models.return_product import ReturnProduct
from django.db import transaction

from book_management.serializers.reserve import ReserveBookSerializer 


class ReturntView(APIView):

    def get(self, request, member_id):
        member = Member.objects.get(id=member_id)
        reserved_items = member.member_reservations.all()
        ser = ReserveBookSerializer(reserved_items, many=True)
        response_data = {"status": "success", "data": ser.data}
        return Response(data=response_data, status=200)

    # def post(self, request, member_id):

    #     payload = request.data.copy()
    #     member = Member.objects.get(id=member_id)
    #     checkout_list = payload.get("checkout_list")
    #     with transaction.atomic():
    #         for checkout_product in checkout_list:
    #             book_id = checkout_product.get("book_id")
    #             number_of_copies = checkout_product.get("number_of_copies")
    #             book: Book = Book.objects.filter(id=book_id).last()
    #             if not book:
    #                 return HttpResponseBadRequest(data="Book id invalid.")
    #             checkout_book = book.book_checkouts.filter(member=member, is_active=True).last()
    #             returned_book = ReturnProduct.objects.filter(book=book, member=member).last()
    #             if number_of_copies > checkout_book - (returned_book.copies if returned_book else 0):
    #                 return HttpResponseBadRequest(content=f"Return order count for {book.name} is greater than the number of order books left.")
    #             if returned_book:
    #                 returned_book.copies += number_of_copies
    #                 returned_book.save()
    #             else:
    #                 ReturnProduct.objects.create(member=member, book=book, copies=number_of_copies)
            
    #     response_data = {"status": "success"}
    #     return Response(data=response_data, status=200)
