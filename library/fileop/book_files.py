import json
from classes.book import Book
def read_books():
    try:
        with open("database/books.json","r") as file:
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
def write_books(books):

    data = []

    for book_data in books:
        data.append({
            "title": book_data.title,
            "author": book_data.author,
            "ISBN": book_data.ISBN,
            "available": book_data.available
        })

    with open("database/books.json", "w") as file:
        json.dump(data, file, indent=4)