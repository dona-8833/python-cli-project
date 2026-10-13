import questionary
from action import add_product


def main():
    while True:
        choice = questionary.select(
            "Select an option:",
            choices=[
                "Add product",
                "Remove product",
                "Update product",
                "Search product",
                "Sell product",
                "Restock product",
                "View inventory",
                "Calculate inventory value",
                "Find low-stock products",
                "Exit"
            ]
        ).ask()

        if choice is None or choice == "Exit":
            print("Goodbye!")
            break

        elif choice == "Add product":
            add_product()
            continue

        elif choice == "Remove product":
            print("Remove product")

        elif choice == "Update product":
            print("Update product")

        elif choice == "Search product":
            print("Search product")

        elif choice == "Sell product":
            print("Sell product")

        elif choice == "Restock product":
            print("Restock product")

        elif choice == "View inventory":
            print("View inventory")

        elif choice == "Calculate inventory value":
            print("Calculate inventory value")

        elif choice == "Find low-stock products":
            print("Find low-stock products")


if __name__ == "__main__":
    main()