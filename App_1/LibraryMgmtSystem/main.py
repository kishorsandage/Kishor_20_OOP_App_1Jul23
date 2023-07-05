'''1.	Library Management System: Create a library management system where
users can add books, borrow and return books, and view available books.'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class LibraryCard:
    def __init__(self, cardNumber, expiryDate):
        self.cardNumber = cardNumber
        self.expiryDate = expiryDate


class LibraryMgmtSystem:
    def __init__(self):
        self.books = []

    def addBook(self,booktoadd):
        #booktoadd = input("Enter book to be added ")
        self.books.append(booktoadd )

    def borrowBook(self, book=None, user=None):
        if book.available:
            book.available = False
            print(f"Book '{book.title}' has been borrowed by {user.name}")
        else:
            print(f"Book '{book.tilt} has already been returned")


    def returnBook(self,book,user):
        if not book.available:
            book.available = True
            print(f"Book '{book.title}' has been returnred by {user.name}")
        else:
            print(f"Book '{book.title}' has already been returned")

    def getAvailableBooks(self):
        available_book = [book for book in self.books if book.available]
        return available_book


# Example usage
system = LibraryMgmtSystem()

book1 = Book("Python Programming", "John Smith")
book2 = Book("Introduction to Java", "Jane Doe")
book3 = Book("Data Science Essentials", "Michael Brown")

system.addBook(book1)
system.addBook(book2)
system.addBook(book3)

user1 = User("Alice", "A001")
user2 = User("Bob", "B002")

system.borrowBook(book1, user1)
system.borrowBook(book2, user2)
system.borrowBook(book3, user1)

system.returnBook(book2, user2)

available_books = system.getAvailableBooks()
print("Available Books:")
for book in available_books:
    print(f"- {book.title} by {book.author}")



