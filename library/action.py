from classes.book import Book
from classes.library import Library
from classes.member import Member
from fileop.book_files import read_books,write_books
from fileop.member_files import read_members,write_members
import random
library = Library()
library.books = read_books()
library.members = read_members(library.books)

# add book
def add_books():
    while True:
        title = input("Enter the book title: ").strip().lower()
        if title:
            break
        print("Book title cannot be empty.")
    while True:
        author = input("Enter author's name: ").strip().lower()
        if author:
            break
        print("Author name cannot be empty.")
    while True:
        ISBN = input("Enter the ISBN for book: ").strip()
        if not ISBN:
            print("ISBN cannot be empty.")
            continue
        try:
            ISBN = int(ISBN)
            break
        except ValueError:
            print("ISBN must be a number.")
    book = Book(title, author, ISBN)
    library.add_books(book)
    write_books(library.books)
# remove books
def remove_books():
    while True:
        book_ISBN = input("Enter the book ISBN you want to remove").strip()
        if not book_ISBN:
            print("Book ISBN cannot be empty")
            continue
        try:
            ISBN = int(book_ISBN)
            break
        except ValueError:
            print("ISBN must be a number")
    book = library.find_books(ISBN)
    if not book:
        print("Book not found")
        return
    library.remove_books(book)
    write_books(library.books)
# search book
def search_books():
    while True:
        query = input("Enter the book title or author name: ").strip().lower()
        if query:
            break
        print("Book title cannot be empty.")
    result = library.search_books(query)
    if not result:
        return
    print()
    print(f"{'Title':<25} {'Author':<25} {'ISBN':<15} ")
    print("-" * 60)
    for book in result:
        print(
            f"{book.title:<25} "
            f"{book.author:<25} "
            f"{book.ISBN:<15} "
        )
# generate member id
def generate_member_id():
    while True:
        member_id = random.randint(100000, 999999)
        if not any(
            member.member_id == member_id
            for member in library.members
        ):
            return member_id
# register member
def register_member():
    while True:
        member_name = input("Enter the member name: ").strip().lower()
        if member_name:
            break
        print("Member name cannot be empty.")
    member_id = generate_member_id()
    member = Member(member_name,member_id)
    library.add_members(member)
    write_members(library.members)
# borrow book
def borrow_books():
    available_books()
    while True:
        query = input("Enter the book title or author name: ").strip().lower()
        if query:
            break
        print("Book title cannot be empty.")
    result = library.search_books(query)
    if not result:
        return
    while True:
        member_id = input("Enter your memberID ").strip()
        if member_id:
            try:
                member_id = int(member_id)
                break
            except ValueError:
                print("member id must be a number")
                continue
        print("member id cannot be empty")
    book = result[0]
    member = library.find_members(member_id)
    if not member:
        return
    library.borrow_book(member,book)
    write_members(library.members)
    write_books(library.books)
# return book
def return_books():
    while True:
        query = input("Enter the book title or author name: ").strip().lower()
        if query:
            break
        print("Book title cannot be empty.")
    result = library.search_books(query)
    if not result:
        return
    while True:
        member_id = input("Enter your memberID ").strip()
        if member_id:
            try:
                member_id = int(member_id)
                break
            except ValueError:
                print("member id must be a number")
                continue
        print("member id cannot be empty")
    book = result[0]
    member = library.find_members(member_id)
    if not member:
        return
    library.return_book(member,book)
    write_members(library.members)
    write_books(library.books)
# available book
def available_books():
    books = library.available_book()
    if not books:
        return
    print()
    print(f"{'Title':<25} {'Author':<25} {'ISBN':<15} ")
    print("-" * 60)
    for book in books:
        print(
            f"{book.title:<25} "
            f"{book.author:<25} "
            f"{book.ISBN:<15} "
        )
# view borrowed book by user
def view_borrowed_books_by_user():
    while True:
        member_id = input("Enter your memberID ").strip()
        if member_id:
            try:
                member_id = int(member_id)
                break
            except ValueError:
                print("member id must be a number")
                continue
        print("member id cannot be empty")
    member = library.find_members(member_id)
    if not member:
        return
    borrowed_book = library.borrowed_books(member)
    if not borrowed_book:
        return
    print()
    print(f"{'Title':<25} {'Author':<25} {'ISBN':<15} ")
    print("-" * 60)
    for book in borrowed_book:
        print(
            f"{book.title:<25} "
            f"{book.author:<25} "
            f"{book.ISBN:<15} "
        )
def view_borrowed_books_from_library_v2():
    books = library.borrowed_book_from_library()
    if not books:
        return
    print()
    print(
        f"{'Title':<25} "
        f"{'Author':<25} "
        f"{'ISBN':<15} "
        f"{'Member':<20} "
        f"{'Member ID':<12}"
    )
    print("-" * 97)
    for book in books:
        print(
            f"{book['title']:<25} "
            f"{book['author']:<25} "
            f"{book['ISBN']:<15} "
            f"{book['member_name']:<20} "
            f"{book['member_id']:<12}"
        )