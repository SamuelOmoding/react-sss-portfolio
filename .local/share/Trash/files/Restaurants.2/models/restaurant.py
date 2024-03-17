# lib/models/Restaurant.py
from models.__init__ import CURSOR, CONN


class Restaurant:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name}, {self.price}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, str) and len(price):
            self._price = price
        else:
            raise ValueError(
                "price must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Restaurant instances """
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Restaurant instances """
        sql = """
            DROP TABLE IF EXISTS restaurants;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and price values of the current Restaurant instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO Restaurants (name, price)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.price))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, price):
        """ Initialize a new Restaurant instance and save the object to the database """
        restaurant = cls(name, price)
        restaurant.save()
        return restaurant

    def update(self):
        """Update the table row corresponding to the current Restaurant instance."""
        sql = """
            UPDATE restaurants
            SET name = ?, price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Restaurant instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM restaurants
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Restaurant object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        restaurant = cls.all.get(row[0])
        if restaurant:
            # ensure attributes match row values in case local instance was modified
            restaurant.name = row[1]
            restaurant.price = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            name = row[1]
            price = row[2] if isinstance(row[2], str) else str(row[2])
            restaurant = cls(name, price)
            restaurant.id = row[0]
            cls.all[restaurant.id] = restaurant
        return restaurant

    @classmethod
    def get_all(cls):
        """Return a list containing a Restaurant object per row in the table"""
        sql = """
            SELECT *
            FROM restaurants
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Restaurant object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM restaurants
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_price(cls, price):
        """Return a Restaurant object corresponding to the table row matching the specified primary key"""
        if not price:
            return None
    
        sql = """
            SELECT *
            FROM restaurants
            WHERE price = ?
        """

        row = CURSOR.execute(sql, (price,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Restaurant object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM restaurants
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def customers(self):
        """Return list of customers associated with current restaurant"""
        from models.customer import Customer
        sql = """
            SELECT * FROM customers
            WHERE restaurant_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Customer.instance_from_db(row) for row in rows
        ]
