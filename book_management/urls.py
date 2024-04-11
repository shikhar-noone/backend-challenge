from django.urls import path, re_path
from book_management.views import *


urlpatterns = [
    re_path('/?$', book.BookListView.as_view(), name='query'),
    re_path('checkout/(?P<member_id>\d+)/?$', checkout.CheckoutView.as_view(), name='query'),
]