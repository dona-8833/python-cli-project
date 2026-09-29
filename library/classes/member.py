
class Member:
    def __init__(self,member_name,member_id):
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = [] 
    def borrow_book(self,book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            return
        print("book is currently unavailable")

    def return_book(self,book):
        if book in self.borrowed_books and not book.available:
            book.return_book()
            self.borrowed_books.remove(book)
            return
        print("book is currently not borrowed member")
    def view_borrowed_book(self):
        result = []
        for book in self.borrowed_books:
            if not book.available:
                result.append(book)
        if not result:
            print("no borrowed books")
            return
        return result