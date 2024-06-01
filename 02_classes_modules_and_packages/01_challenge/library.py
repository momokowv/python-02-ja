# ここにコードを書いてください
class Library:
    
    def __init__(self):
        self.book_shelf=[]
    
    def add_book(self, title, author):
        book={"title":title, "author":author}
        self.book_shelf.append(book)
        return self.book_shelf
        
    def remove_book(self, title):
        for book in self.book_shelf:
            if book["title"] == title:
                self.book_shelf.remove(book)
                return self.book_shelf
    
    def retrieve_books(self):
        return self.book_shelf


my_library = Library()
my_library.add_book("1984", "George Orwell")
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
for book in my_library.retrieve_books():
    print(book)
my_library.remove_book("1984")
for book in my_library.retrieve_books():
    print(book)