import json
from classes.member import Member
from classes.book import Book

def write_members(members):
        data = []
        for member in members:
            data.append({
                "member_name":member.member_name,
                "member_id":member.member_id,
                "borrowed_books":[book.ISBN for book in member.borrowed_books]
            })
        with open("database/members.json","w") as file:
            json.dump(data,file,indent=4)

def read_members(books):
    try:
        with open("database/members.json", "r") as file:
            data = json.load(file)
            members = []
            for member_data in data:
                member = Member(
                    member_data["member_name"],
                    member_data["member_id"]
                )
                for ISBN in member_data["borrowed_books"]:
                    for book in books:
                        if book.ISBN == ISBN:
                            member.borrowed_books.append(book)
                            break
                members.append(member)
            return members
    except (FileNotFoundError, json.JSONDecodeError):
        return []