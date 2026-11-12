from book import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_book(self):
        for book in self.books:

            print(f"_____{book.get_info()}_________")


if __name__ == "main":
    print("testing the library ")
    Lib = Library("The Queen's")
    my_book = Book("python 101", "Moeen")
    Lib.add_book(my_book)
    print(Lib.list_book())
