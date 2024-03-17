# lib/models/Customer.py
from models.__init__ import CURSOR, CONN
# from models.restaurant import Restaurant


class Customer:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<Customer {self.id}: {self.first_name}, {self.last_name}>"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name):
            self._first_name = first_name
        else:
            raise ValueError(
                "first_name must be a non-empty string"
            )

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name):
            self._last_name = last_name
        else:
            raise ValueError(
                "last_name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Customer instances """
        sql = """
            CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            Restaurant_id INTEGER,
            FOREIGN KEY (Restaurant_id) REFERENCES Restaurants(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Customer instances """
        sql = """
            DROP TABLE IF EXISTS Customers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the first_name, job title, and Restaurant id values of the current Customer object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO Customers (first_name, last_name, Restaurant_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.Restaurant_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Customer instance."""
        sql = """
            UPDATE Customers
            SET first_name = ?, last_name = ?, Restaurant_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name,
                             self.Restaurant_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Customer instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM Customers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, first_name, last_name):
        """ Initialize a new Customer instance and save the object to the database """
        Customer = cls(first_name, last_name)
        Customer.save()
        return Customer

    @classmethod
    def instance_from_db(cls, row):
        """Return an Customer object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        Customer = cls.all.get(row[0])
        if Customer:
            # ensure attributes match row values in case local instance was modified
            Customer.first_name = row[1]
            Customer.last_name = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            Customer = cls(row[1], row[2])
            Customer.id = row[0]
            cls.all[Customer.id] = Customer
        return Customer

    @classmethod
    def get_all(cls):
        """Return a list containing one Customer object per table row"""
        sql = """
            SELECT *
            FROM Customers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Customer object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM Customers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_first_name(cls, first_name):
        """Return Customer object corresponding to first table row matching specified first_name"""
        sql = """
            SELECT *
            FROM Customers
            WHERE first_name is ?
        """

        row = CURSOR.execute(sql, (first_name,)).fetchone()
        return cls.instance_from_db(row) if row else None
