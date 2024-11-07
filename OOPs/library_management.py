'''
Library Management
•	Create a class called Library with attributes:
        o	library_name: Name of the library.
        o	books: A list to store the books available in the library.
•	Write methods to:
        o	Add a book to the library.
        o	Remove a book from the library.
        o	Display all books in the library.
•	Create a Library instance, add books, remove a book, and list all available books.
'''

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.book = []
    
    def book_add(self, book_title):
        self.book.append(book_title)
        print(f"The book '{book_title}' has been added to the library.")
    
    def book_remove(self, book_title):
        if (book_title in self.book):
            self.book.remove(book_title)
            print(f"The book '{book_title}' has been removed from the library.")
        else:
            print(f"The book '{book_title}' is not found in the library.")
    
    def display_books(self):
        if self.book:
            print(f"Books which are available in '{self.library_name}':")
            for book in self.book:
                print(f"- {book}")
        else:
            print(f"No books available in '{self.library_name}'.")

my_library = Library("Silent Scholar center")

my_library.book_add("The Catcher in the Rye")
my_library.book_add("1984")
my_library.book_add("To Kill a Mockingbird")

my_library.display_books()

my_library.book_remove("1984")

my_library.display_books()

my_library.book_remove("The Great Gatsby")            #A book that is not available in the library.