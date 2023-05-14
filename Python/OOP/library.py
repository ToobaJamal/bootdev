'''
Book class
__init__(self, title, author)
Set .title and .author to the values of the parameters.

Library class
Add the following methods.

__init__(self, name)
Initialize a .name member variable to the value of the name parameter. Create a .books member initialized to an empty list.

add_book(self, book)
Add the book to the books instance variable by appending it to the end of the list.

remove_book(self, book)
If the book is in the library, the remove_book method should remove it from the list.

search_books(self, search_string)
For every book in the library check if the search_string is contained in the title or author field (case insensitive). 
Return a list of all books that match the search string, ordered in the same order as they were added to the library.
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
       self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_books(self, search_strings):
        searched_books = []
        for book in self.books:
            if search_strings.lower() in book.title.lower() or search_strings.lower() in book.author.lower():
                searched_books.append(book)
        return searched_books
            
        
