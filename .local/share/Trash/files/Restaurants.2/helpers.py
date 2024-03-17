from models.restaurant import Restaurant
from models.customer import Customer


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the restaurant functions in this lesson

def list_restaurants():
    restaurants = Restaurant.get_all()
    for restaurant in restaurants:
        print(restaurant)


def find_restaurant_by_name():
    name = input("Enter the restaurant's name: ")
    restaurant = Restaurant.find_by_name(name)
    print(restaurant) if restaurant else print(
        f'Restaurant {name} not found')


def find_restaurant_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the restaurant's id: ")
    restaurant = Restaurant.find_by_id(id_)
    print(restaurant) if restaurant else print(f'Restaurant {id_} not found')

def find_restaurant_by_price():
    #use a trailing underscore not to override the built-in id function
    price_ = input("Enter the restaurant's price: ")
    restaurant = Restaurant.find_by_price(price_)
    print(restaurant) if restaurant else print(f'Restaurant {price_} not found')


def create_restaurant():
    name = input("Enter the restaurant's name: ")
    price = input("Enter the restaurant's price: ")
    try:
        restaurant = Restaurant.create(name, price)
        print(f'Success: {restaurant}')
    except Exception as exc:
        print("Error creating restaurant: ", exc)


def update_restaurant():
    id_ = input("Enter the restaurant's id: ")
    if restaurant := Restaurant.find_by_id(id_):
        try:
            name = input("Enter the restaurant's new name: ")
            restaurant.name = name
            price = input("Enter the restaurant's new price: ")
            restaurant.price = price

            restaurant.update()
            print(f'Success: {restaurant}')
        except Exception as exc:
            print("Error updating restaurant: ", exc)
    else:
        print(f'Destaurant {id_} not found')


def delete_restaurant():
    id_ = input("Enter the restaurant's id: ")
    if restaurant := Restaurant.find_by_id(id_):
        restaurant.delete()
        print(f'Restaurant {id_} deleted')
    else:
        print(f'Restaurant {id_} not found')


def list_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)
    pass


def find_customer_by_first_name():
    first_name = input("Enter the customer's first_name: ")
    customer = Customer.find_by_first_name(first_name)
    print(customer) if customer else print(
        f'Customer {first_name} not found')
pass


def find_customer_by_id():
    id_ = input("Enter the customer's id: ")
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f'Customer {id_} not found')
    pass


def create_customer():    
    first_name = input("Enter the customer's first_name: ")
    last_name = input("Enter the last_name: ")
    try:
        customer = Customer.create(first_name, last_name)
        print(f'Success: {customer}')
    except Exception as exc:
        print("Error creating customer: ", exc)
pass


def update_customer(customer_id, first_name=None, last_name=None):
    customer = Customer.all_customers.get(customer_id)
    if not customer:
        return "customer not found"
    if first_name is not None:
        customer.first_name = first_name
    if last_name is not None:
        customer.last_name = last_name
    return "Customer updated successfully"
pass


def delete_customer():
    id_ = input("Enter the customer's id: ")
    if customer:= Customer.find_by_id(id_):
        customer.delete()
        print(f'Customer {id_} deleted')
    else:
        print(f'Customer {id_} not found')
    pass


def list_restaurant_customers(restaurant_id):
    restaurant_customers = []
    for customer in Customer.all_customers.values():
        if customer.restaurant_id == restaurant_id:
            restaurant_customers.append(customer)
    return restaurant_customers
pass