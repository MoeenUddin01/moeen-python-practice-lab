class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checkout = True

    def get_info(self):
        if self.is_checkout:
            status = "Not_available"
        else:
            status = "Available"
        return f"{self.title} by {self.author} {status}"


if __name__ == "__main__":
    print("running self testing form book.py")
    b = Book("the kings", "Moeen")
    print(b.get_info())
