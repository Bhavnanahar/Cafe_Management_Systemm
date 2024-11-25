def display_menu():
    print("Menu:")
    print("1. Pizza - Rs. 100")
    print("2. Sandwich - Rs. 200")
    print("3. Garlic Bread - Rs. 300")
    print("4. Cold Drink - Rs. 250")

def take_order():
    name = input("Enter your name: ")
    total_bill = 0

    while True:
        display_menu()
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            total_bill += 100
        elif choice == 2:
            total_bill += 200
        elif choice == 3:
            total_bill += 300
        elif choice == 4:
            total_bill += 250
        else:
            print("Invalid choice. Please try again.")
            continue

        more_items = input("Do you want to add more items? (yes/no): ")
        if more_items.lower() != "yes":
            break

    print("\nOrder Summary for", name)
    print("Total Bill: Rs.", total_bill)

if __name__ == "__main__":
    take_order()