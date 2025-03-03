class BookNotFoundException(Exception):
    def __init__(self, title):
        self.message = f"Book '{title}' not found in the library."
        super().__init__(self.message)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, title):
        self.message = f"Book '{title}' is already borrowed."
        super().__init__(self.message)

class MemberLimitExceededException(Exception):
    def __init__(self, name):
        self.message = f"Member '{name}' has reached the borrowing limit."
        super().__init__(self.message)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.borrow_limit = 3

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit:
            raise MemberLimitExceededException(self.name)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book.title)
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(book_title)
        try:
            member.borrow_book(book)
            print(f"{member.name} borrowed '{book.title}'.")
        except (BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        if not book:
            print(f"Book '{book_title}' not borrowed by {member.name}.")
            return
        member.return_book(book)
        print(f"{member.name} returned '{book.title}'.")


lib = Library()


book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Brave New World", "Aldous Huxley")
member1 = Member("Alice")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_member(member1)

try:
    lib.borrow_book("Alice", "1984")
    lib.borrow_book("Alice", "To Kill a Mockingbird")
    lib.borrow_book("Alice", "Brave New World")
    lib.borrow_book("Alice", "Unknown Book")  # Should raise BookNotFoundException
except Exception as e:
    print(e)


lib.return_book("Alice", "1984")
lib.return_book("Alice", "The Hobbit")  # Not borrowed, should print a message

try:
    lib.borrow_book("Alice", "1984")
    lib.borrow_book("Alice", "To Kill a Mockingbird")
    lib.borrow_book("Alice", "Brave New World")
    lib.borrow_book("Alice", "The Great Gatsby")  # Exceeds limit
except Exception as e:
    print(e)

try:
    lib.borrow_book("Alice", "1984")  # Already borrowed
except Exception as e:
    print(e)
