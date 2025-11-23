def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    # shopping_list must be a list
    shopping_list = []

    while True:
        # call display_menu each loop
        display_menu()

        # choice must be taken as a NUMBER (int)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Add item
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added.")

        elif choice == 2:
            # Remove item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print("Item not found in list.")

        elif choice == 3:
            # View list
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
