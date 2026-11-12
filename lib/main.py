from book import Book
from library import Library


def main():
    book1 = Book("clearn code", "Robert C. mertin")
    book2 = Book("Automate the boring stuff", "Al swigart")

    my_library = Library("Tech_Community")

    my_library.add_book(book1)
    my_library.add_book(book2)

    my_library.list_book()


if __name__ == "__main__":
    main()
