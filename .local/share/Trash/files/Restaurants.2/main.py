import sqlite3

CONN = sqlite3.connect('restaurant.db')
CURSOR = CONN.cursor()
class Restaurant:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def reviews(self):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("SELECT * FROM reviews WHERE restaurant_id=?", (self.id,))
        reviews = c.fetchall()
        conn.close()
        return reviews

    def customers(self):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("SELECT customers.* FROM customers INNER JOIN reviews ON customers.id = reviews.customer_id WHERE reviews.restaurant_id=?", (self.id,))
        customers = c.fetchall()
        conn.close()
        return customers

    @classmethod
    def fanciest(cls):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("SELECT * FROM restaurants ORDER BY price DESC LIMIT 1")
        fanciest_restaurant = c.fetchone()
        conn.close()
        if fanciest_restaurant:
            return cls(*fanciest_restaurant)
        else:
            return None

    def all_reviews(self):
        reviews = self.reviews()
        formatted_reviews = []
        for review in reviews:
            customer = Customer.find_by_id(review[2])
            formatted_review = f"Review for {self.name} by {customer.full_name()}: {review[3]} stars."
            formatted_reviews.append(formatted_review)
        return formatted_reviews
    
        
    
class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def reviews(self):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("SELECT * FROM reviews WHERE customer_id=?", (self.id,))
        reviews = c.fetchall()
        conn.close()
        return reviews

    def restaurants(self):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("SELECT restaurants.* FROM restaurants INNER JOIN reviews ON restaurants.id = reviews.restaurant_id WHERE reviews.customer_id=?", (self.id,))
        restaurants = c.fetchall()
        conn.close()
        return restaurants

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        reviews = self.reviews()
        if not reviews:
            return None
        max_rating = max(review[3] for review in reviews)
        favorite_review = [review for review in reviews if review[3] == max_rating][0]
        favorite_restaurant = Restaurant.find_by_id(favorite_review[1])
        return favorite_restaurant

    def add_review(self, restaurant, rating):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)", (restaurant.id, self.id, rating))
        conn.commit()
        conn.close()

    def delete_reviews(self, restaurant):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("DELETE FROM reviews WHERE restaurant_id=? AND customer_id=?", (restaurant.id, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, customer_id):
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("SELECT * FROM customers WHERE id=?", (customer_id,))
        customer = c.fetchone()
        conn.close()
        if customer:
            return cls(*customer)
        else:
            return None
        
        
class Review:
    def __init__(self, id, restaurant_id, customer_id, star_rating):
        self.id = id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating

    def customer(self):
        return Customer.find_by_id(self.customer_id)

    def restaurant(self):
        return Restaurant.find_by_id(self.restaurant_id)

    def full_review(self):
        customer = self.customer()
        restaurant = self.restaurant()
        return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."




