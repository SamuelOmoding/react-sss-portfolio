class Review:
    def __init__(self, restaurant_id, customer_id, star_rating):
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating

    def customer(self):
        cursor.execute('SELECT * FROM customers WHERE id = ?', (self.customer_id,))
        row = cursor.fetchone()
        return Customer(*row)

    def restaurant(self):
        cursor.execute('SELECT * FROM restaurants WHERE id = ?', (self.restaurant_id,))
        row = cursor.fetchone()
        return Restaurant(*row)

    def full_review(self):
        return f'Review for {self.restaurant().name} by {self.customer().full_name()}: {self.star_rating} stars.'
