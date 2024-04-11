from django.db import models
from book_management.models.member import Member
from book_management.models.book import Book

class ReturnProduct(models.Model):

    # checkout id will be autogenerated
    member = models.ForeignKey(to=Member, related_name="member_returns", on_delete=models.PROTECT)
    book = models.ForeignKey(to=Book, related_name="book_returns", on_delete=models.PROTECT)
    copies = models.IntegerField()
    