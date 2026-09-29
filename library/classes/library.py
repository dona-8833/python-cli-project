class Library:
    def __init__(self):
        self.members = []
        self.books = []
    def add_books(self,book):
        ISBN_codes = [book.ISBN for book in self.books]
        if book.ISBN in ISBN_codes:
            print("cannot add book due to duplicate")
            return
        self.books.append(book)
        print("Book added successfully")
    def add_members(self,member):
        member_ids = [member.member_id for member in self.members]
        if member.member_id not in member_ids:
            self.members.append(member)
            return
        print("member already available")
    def remove_books(self,book):
        if book not in self.books:
            print("cannot remove invalid book")
            return
        if not book.available:
            print("you cannot remove a borrowed book")
            return
        self.books.remove(book)
        print("book successfully removed")
    def find_books(self,ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        print("book not in library")
    def find_members(self,member_id): 
        for member in self.members:
            if member.member_id == member_id:
                return member
        print("member not registered")
    def search_books(self,query):
        result = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                result.append(book)
        if not result:
            print("book not found")
        return result
    def borrow_book(self, member, book):
        if member not in self.members:
            print("You are not a member of our library")
            return
        if book not in self.books:
            print("Book not in library")
            return
        if not book.available:
            print("Book is already borrowed")
            return
        member.borrow_book(book)
    def return_book(self,member,book):
        if member not in self.members:
            print("you are not a member of our library")
            return
        if book not in self.books:
            print("Book not in library")
            return
        if book.available:
            print("book was not borrowed")
            return
        member.return_book(book)
    def available_book(self):
        result = []
        for book in self.books:
            if book.available:
                result.append(book)
        if not result:
            print("no available book")
            return
        return result
    def borrowed_books(self,member):
        if member not in self.members:
            print("you are not a member of our library")
            return
        return member.view_borrowed_book()
    def borrowed_book_from_library(self):
        borrowed_books = []
        result = []
        for book in self.books:
            if not book.available:
                borrowed_books.append(book)
        if not borrowed_books:
            print("no available")
            return
        for book in borrowed_books:
            for member in self.members:
                if book in member.borrowed_books:
                    book_data = {
                        "title":book.title,
                        "author" : book.author,
                        "ISBN" : book.ISBN,
                        "member_name" : member.member_name,
                        "member_id" : member.member_id
                    }
                    result.append(book_data)
        if not result:
            print("no borrowed book available")
            return
        return result