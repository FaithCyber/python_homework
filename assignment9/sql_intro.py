import sqlite3


# Task 1: Create a New SQLite Database


try:
    conn = sqlite3.connect("../db/magazines.db")
    cursor = conn.cursor()

    # Task 2: Define Database Structure

    # Generate publishers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)

    # Generate magazines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id)
            REFERENCES publishers(publisher_id)
    )
    """)

    # Generate subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    # Generate subscriptions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id)
            REFERENCES subscribers(subscriber_id),
        FOREIGN KEY (magazine_id)
            REFERENCES magazines(magazine_id)
    )
    """)

      
    # Task 3: Populate Tables with Data

    def add_publisher(name):
        try:
            cursor.execute(
                "SELECT * FROM publishers WHERE name = ?",
                (name,)
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO publishers (name) VALUES (?)",
                    (name,)
                )

        except sqlite3.Error as e:
            print("Publisher error:", e)


    def add_magazine(name, publisher_id):
        try:
            cursor.execute(
                "SELECT * FROM magazines WHERE name = ?",
                (name,)
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                    (name, publisher_id)
                )

        except sqlite3.Error as e:
            print("Magazine error:", e)


    def add_subscriber(name, address):
        try:
            cursor.execute(
                "SELECT * FROM subscribers WHERE name = ? AND address = ?",
                (name, address)
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO subscribers (name, address) VALUES (?, ?)",
                    (name, address)
                )

        except sqlite3.Error as e:
            print("Subscriber error:", e)


    def add_subscription(subscriber_id, magazine_id, expiration_date):
        try:
            cursor.execute("""
                SELECT * FROM subscriptions
                WHERE subscriber_id = ?
                AND magazine_id = ?
                AND expiration_date = ?
            """, (subscriber_id, magazine_id, expiration_date))

            if cursor.fetchone() is None:
                cursor.execute("""
                    INSERT INTO subscriptions
                    (subscriber_id, magazine_id, expiration_date)
                    VALUES (?, ?, ?)
                """, (subscriber_id, magazine_id, expiration_date))

        except sqlite3.Error as e:
            print("Subscription error:", e)

    # Add publishers
    add_publisher("Time Inc")
    add_publisher("National Geographic")
    add_publisher("Conde Nast")

    # Add magazines
    add_magazine("Time", 1)
    add_magazine("National Geographic Magazine", 2)
    add_magazine("Vogue", 3)

    # Add subscribers
    add_subscriber("John Smith", "123 Main St")
    add_subscriber("Mary Jones", "456 Oak Ave")
    add_subscriber("David Brown", "789 Pine Rd")

    # Add subscriptions
    add_subscription(1, 1, "2027-01-01")
    add_subscription(2, 2, "2027-02-01")
    add_subscription(3, 3, "2027-03-01")

# Task 4: Write SQL Queries


print("\n--- All Subscribers ---")
try:
    cursor.execute("SELECT * FROM subscribers")
    subscribers = cursor.fetchall()
    for row in subscribers:
        print(row)
except sqlite3.Error as e:
    print("Query error (subscribers):", e)


print("\n--- All Magazines (Sorted by Name) ---")
try:
    cursor.execute("SELECT * FROM magazines ORDER BY name ASC")
    magazines = cursor.fetchall()
    for row in magazines:
        print(row)
except sqlite3.Error as e:
    print("Query error (magazines):", e)


print("\n--- Magazines for a Specific Publisher (JOIN) ---")
try:
    publisher_name = "Time Inc"   # change if you want a different one

    cursor.execute("""
        SELECT magazines.magazine_id, magazines.name, publishers.name
        FROM magazines
        JOIN publishers
        ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
    """, (publisher_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)

except sqlite3.Error as e:
    print("Query error (join):", e)