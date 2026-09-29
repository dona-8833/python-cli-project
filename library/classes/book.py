class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available =  True
    def borrow(self):
        if self.available:
            self.available = False
            return
        print("book is currently unavailable")
    def return_book(self):
        if not self.available:
            self.available = True
            print("book successfully returned")
            return
        print("book is currently not borrowed")