from action import add_books , remove_books , search_books,register_member , borrow_books , return_books , available_books,view_borrowed_books_by_user, view_borrowed_books_from_library_v2

def continue_or_exit():
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter y or n")

def main():

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
[8] View borrowed books from user
[9] view borrowed books from library
[0] Exit
""")

        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("\nPlease enter a number.")
            continue

        if choice == 1:
            add_books()
        elif choice == 2:
            remove_books()
        elif choice == 3:
            search_books()
        elif choice == 4:
            register_member()
        elif choice == 5:
            borrow_books()
        elif choice == 6:
            return_books()
        elif choice == 7:
            available_books()
        elif choice == 8:
            view_borrowed_books_by_user()
        elif choice == 9:
            view_borrowed_books_from_library_v2()
        elif choice == 0:
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

        if not continue_or_exit():
            print("Goodbye!")
            return

if __name__ == "__main__":
    main()