class Book:
    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"{book.title} borrowed successfully.")
                else:
                    print(f"{book.title} is  not available.")
                print(f"{book.title} not found in the library.")
    def display_books(self):
        print("books in library:")
        for book in self.books:
            status = "Available" if book.available else "Checked Out"
            print(f"{book.title} - {status}")

library = Library()
x = Book("bla", "james")
library.add_book(x)
library.borrow_book("james")
library.display_books()