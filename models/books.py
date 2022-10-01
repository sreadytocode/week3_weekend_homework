from types import TracebackType
from models.book import *
import datetime


book1 = Book("Dune", "Frank Herbert", "Science Fiction", True, datetime.date(2022, 5, 15))
book2 = Book("The Witcher: Blood of Elves", "Andrzej Sapkowski", "Fantasy", False, datetime.date(2022, 7, 2))
book3 = Book("Crime and Punishment", "Fyodor Dostoyevsky", "Classic", True, datetime.date(2022, 4, 19))

books=[book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)
