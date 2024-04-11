from book_management.models.book import Book


class BookService():

    def add_new_book(name, number_of_copies):
        new_book = Book.objects.create(
            name=name, 
            number_of_copies=number_of_copies
        )
        return new_book

    def add_copies_of_book(name, number_of_copies):
        new_book = Book.objects.create(
            name=name, 
            number_of_copies=number_of_copies
        )
        return new_book