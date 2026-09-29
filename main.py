import json

def write_books(books):

        data = []
        for book in books:
            data.append({
                "title":book.title,
                "author": book.author,
                "ISBN": book.ISBN,
                "available": book.available
            })
        
        with open("books.json","w") as file:
            json.dump(data,file,indent=4)

def read_books():
    try:
        with open("books.json","r") as file:
            data = json.load(file)
            books = []
            for book_data in data:
                book = Book(
                    book_data["title"],
                    book_data["author"],
                    book_data["ISBN"]
                )
                book.available = book_data["available"]
                books.append(book)
            return books
    except (FileNotFoundError,json.JSONDecodeError):
        return []

def write_members(members):
        data = []
        for member in members:
            data.append({
                "member_name":member.name,
                "member_id":member.member_id,
                "borrowed_books":member.borrowed_books
            })
        with open("members.json","w") as file:
            json.dump(data,file,indent=4)

def read_members():
    try:
        with open("members.json","r") as file:
            data = json.load(file)
            members = []
            for member_data in data:
                member = Member(
                    member_data["name"],
                    member_data["member_id"]
                )
                member.borrowed_books = member_data["borrowed_books"]
                members.append(member)
            return members
    except (FileNotFoundError,json.JSONDecodeError):
        return []

class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True
    def borrow(self):
        if (self.available):
            self.available = False
        else:
            print("book is already borrowed")
    def return_book(self):
        if (self.available):
            print("book is not currently borrowed")
        else:
            self.available = True

class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books=[]
    def borrow_book(self, book):
        if not book.available:
            print("the book isn't available")
            return
        book.borrow()
        self.borrowed_books.append(book)
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("you haven't borrowed that book.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        ISBN_codes = [book.ISBN for book in self.books]
        if book.ISBN in ISBN_codes:
            print("same ISBN number")
        else:
            self.books.append(book)
    def register_member(self, member):
        member_id = [mem.member_id for mem in self.members]
        if member.member_id in member_id:
            print("same member id")
        else:
            self.members.append(member)
    def search_books(self, query):
        result = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                result.append(book)
        if not result:
            print("book not found")
        return result
    def available_books(self):
        result = []
        for book in self.books:
            if book.available :
                result.append(book)
        if not result:
            print("no availabe books")
        return result
    def borrow_book(self, member, book):
        if member in self.members and book in self.books:
            member.borrow_book(book)
        else:
            if member not in self.members:
                print("you are not a member of our library")
            elif book not in self.books:
                print("book not in library") 
    def return_book(self, member, book):
        if member not in self.members:
            print("you are not part of our library")
            return
        if book not in self.books:
            print("this is not our book")
            return
        member.return_book(book)
    def remove_book(self, book):
        if book not in self.books:
            print("book not present")
            return
        if not book.available:
            print("you cant return burrrowed book")
            return
        self.books.remove(book)
    def borrowed_books(self):
        borrowed_books_list = []
        for member in self.members:
            if bool(member.borrowed_books):
                borrowed_books_list.extend(member.borrowed_books)
        if not borrowed_books_list:
            print("no borrowed books")
            return
        return borrowed_books_list
    def find_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        return None


def main():

    library = Library()

    library.books = read_books()
    library.members = read_members()

    while True:

        print("""
=============================
      LIBRARY MANAGEMENT
=============================

[1] Add books
[2] Remove books
[3] Search for books
[4] Register members
[5] Borrow books
[6] Return books
[7] View available books
[8] View borrowed books
[0] Exit
""")

        choice = input("Select an option: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            ISBN = input("Enter ISBN: ").strip()
            book = Book(title, author, ISBN)
            library.add_book(book)
            write_books(library.books)
        elif choice == "2":
            ISBN = input("Enter ISBN of the book: ").strip()
            book = library.find_book(ISBN)
            if not book:
                print("Book not found.")
                continue
            library.remove_book(book)
            write_books(library.books)
        elif choice == "3":
            query = input("enter the name or author of the book").strip()
            books = library.search_books(query)
            if not books:
                continue
            for book in books:
                print(
                    f"Title: {book.title} | "
                    f"Author: {book.author} | "
                    f"ISBN: {book.ISBN} | "
                    f"Available: {book.available}"
                )
        elif choice == "4":
            member_name = input("Enter member name ").strip()
            member_id = input("enter member id ").strip()
            member = Member(member_name,member_id)
            library.register_member(member)
            write_members(library.members)

        elif choice == "5":
            # member_id = input("Enter member ID: ").strip()
            # ISBN = input("Enter ISBN of the book: ").strip()
            # member = library.find_member(member_id)
            # book = library.find_book(ISBN)
            # if not member:
            #     print("Member not found.")
            #     continue
            # if not book:
            #     print("Book not found.")
            #     continue
            # library.borrow_book(member, book)
            # write_members(library.members)
            # write_books(library.books)
            pass
        elif choice == "6":
            pass

        elif choice == "7":
            pass

        elif choice == "8":
            pass

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()