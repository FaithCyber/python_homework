import sqlite3

# =========================
# Task 1 & 2 & 3 & 4
# =========================

try:
    # Task 1: Connect DB
    conn = sqlite3.connect("../db/magazines.db")
    cursor = conn.cursor()

    # Task 2: Enable foreign keys
    conn.execute("PRAGMA foreign_keys = 1")

    # -------------------------
    # Create Tables
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id)
            REFERENCES publishers(publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

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

    # -------------------------
    # Task 3: Insert Functions
    # -------------------------

    def add_publisher(name):
        cursor.execute("SELECT * FROM publishers WHERE name = ?", (name,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))

    def add_magazine(name, publisher_id):
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id)
            )

    def add_subscriber(name, address):
        cursor.execute(
            "SELECT * FROM subscribers WHERE name = ? AND address = ?",
            (name, address)
        )
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO subscribers (name, address) VALUES (?, ?)",
                (name, address)
            )

    def add_subscription(subscriber_id, magazine_id, expiration_date):
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

    # -------------------------
    # Insert Data
    # -------------------------

    add_publisher("Time Inc")
    add_publisher("National Geographic")
    add_publisher("Conde Nast")

    add_magazine("Time", 1)
    add_magazine("National Geographic Magazine", 2)
    add_magazine("Vogue", 3)

    add_subscriber("John Smith", "123 Main St")
    add_subscriber("Mary Jones", "456 Oak Ave")
    add_subscriber("David Brown", "789 Pine Rd")

    add_subscription(1, 1, "2027-01-01")
    add_subscription(2, 2, "2027-02-01")
    add_subscription(3, 3, "2027-03-01")

    # =========================
    # Task 4: Queries
    # =========================

    print("\n--- All Subscribers ---")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\n--- Magazines Sorted ---")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    print("\n--- Magazines by Publisher (JOIN) ---")
    cursor.execute("""
        SELECT magazines.name, publishers.name
        FROM magazines
        JOIN publishers
        ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = 'Time Inc'
    """)
    for row in cursor.fetchall():
        print(row)

    conn.commit()
    print("\nDatabase updated successfully.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")