
from helpers import (
    exit_program,
    list_restaurants,
    find_restaurant_by_name,
    find_restaurant_by_id,
    find_restaurant_by_price,
    create_restaurant,
    update_restaurant,
    delete_restaurant,
    list_customers,
    find_customer_by_first_name,
    find_customer_by_id,
    create_customer,
    update_customer,
    delete_customer,
    list_restaurant_customers
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_restaurants()
        elif choice == "2":
            find_restaurant_by_name()
        elif choice == "3":
            find_restaurant_by_id()
        elif choice == "4":
            find_restaurant_by_price()
        elif choice == "5":
            create_restaurant()
        elif choice == "6":
            update_restaurant()
        elif choice == "7":
            delete_restaurant()
        elif choice == "8":
            list_customers()
        elif choice == "9":
            find_customer_by_first_name()
        elif choice == "10":
            find_customer_by_id()
        elif choice == "11":
            create_customer()
        elif choice == "12":
            update_customer()
        elif choice == "13":
            delete_customer()
        elif choice == "14":
            list_restaurant_customers()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all restaurants")
    print("2. Find restaurant by name")
    print("3. Find restaurant by id")
    print("4. Find restaurant by price")
    print("5: Create restaurant")
    print("6: Update restaurant")
    print("7: Delete restaurant")
    print("8. List all customers")
    print("9. Find customer by name")
    print("10. Find customer by id")
    print("11: Create customer")
    print("12: Update customer")
    print("13: Delete customer")
    print("14: List all customers in a restaurant")


if __name__ == "__main__":
    main()
