'''
class = book
attributes = title, author and page
there is a default constructor
new method set details
new method display details
new method is valid or not ( for valid pages should be greater than 300.)
there will be 2 instance for book class
'''

class Book:
    def __init__(self, title = " ", author = " ", page = 0):
        self.title = title
        self.author = author
        self.page = page 

    def set_detail(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page 

    def display_detail(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Pages: ", self.page)

    def is_valid_ornot(self):
        return self.page > 300
    
book1 = Book()
book2 = Book()

book1.set_detail("The Lord of the Rings", "J.R.R. Tolkien", 1178)
book2.set_detail("Pride and Prejudice", "Jane Austen", 424)

book1.display_detail()
print("Valid: ", book1.is_valid_ornot())

book2.display_detail()
print("Valid: ", book2.is_valid_ornot())