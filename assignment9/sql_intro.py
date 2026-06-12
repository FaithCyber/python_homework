# Task 1: Create a New SQLite Database


import sqlite3

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Task 2: Define Database Structure

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id)
            REFERENCES publishers(publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id)
            REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id)
            REFERENCES magazines(magazine_id)
        )
        """)

        # ======================================
        # Task 3: Populate Tables with Data
        # ======================================

        def add_publisher(name):
            try:
                cursor.execute(
                    "INSERT INTO publishers (name) VALUES (?)",
                    (name,)
                )
            except sqlite3.IntegrityError:
                pass

        def add_magazine(name, publisher_id):
            try:
                cursor.execute(
                    "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                    (name, publisher_id)
                )
            except sqlite3.IntegrityError:
                pass

        def add_subscriber(name, address):
            cursor.execute(
                "SELECT * FROM subscribers WHERE name=? AND address=?",
                (name, address)
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO subscribers (name, address) VALUES (?, ?)",
                    (name, address)
                )

        add_publisher("Time Inc")
        add_publisher("National Geographic")
        add_publisher("Condé Nast")

        add_magazine("Time", 1)
        add_magazine("National Geographic Magazine", 2)
        add_magazine("Vogue", 3)

        add_subscriber("John Smith", "123 Main St")
        add_subscriber("Jane Doe", "456 Oak Ave")
        add_subscriber("Bob Wilson", "789 Pine Rd")

        conn.commit()

        # ======================================
        # Task 4: Write SQL Queries
        # ======================================

        print("\nAll Subscribers")
        cursor.execute("SELECT * FROM subscribers")
        for row in cursor.fetchall():
            print(row)

        print("\nMagazines Sorted By Name")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        for row in cursor.fetchall():
            print(row)

        print("\nMagazines Published By Time Inc")
        cursor.execute("""
        SELECT m.name
        FROM magazines m
        JOIN publishers p
        ON m.publisher_id = p.publisher_id
        WHERE p.name = 'Time Inc'
        """)

        for row in cursor.fetchall():
            print(row)

except sqlite3.Error as e:
    print("Database Error:", e)

print("Connection closed.")

    
  