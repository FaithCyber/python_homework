import sqlite3
import os

def main():
    # TARGETING THE CORRECT DATABASE WITH 100 CUSTOMERS:
    db_path = r"C:\Users\Gambr\python_homework\db\lesson.db"
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Enforce foreign key constraints
    conn.execute("PRAGMA foreign_keys = 1")
    
    # Task 1: Complex JOINs with Aggregation

    print("--- Task 1: Total Price of Each of the First 5 Orders ---")
    
    task1_query = """
        SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id ASC
        LIMIT 5;
    """
    
    cursor.execute(task1_query)
    task1_results = cursor.fetchall()
    
    for row in task1_results:
        print(f"Order ID: {row[0]} | Total Price: ${row[1]:.2f}")
    print("\n")

    # Task 2: Understanding Subqueries
   
    print("--- Task 2: Average Order Price per Customer ---")
    
    task2_query = """
        SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) sub ON c.customer_id = sub.customer_id_b
        GROUP BY c.customer_id;
    """
    
    cursor.execute(task2_query)
    task2_results = cursor.fetchall()
    
    for row in task2_results:
        avg_price = f"${row[1]:.2f}" if row[1] is not None else "$0.00"
        print(f"Customer: {row[0]} | Avg Order Price: {avg_price}")
    print("\n")

    # Task 3: An Insert Transaction Based on Data
   
    print("--- Task 3: Insert Transaction & Verification ---")
    
    try:
        # 1. Fetch Customer ID
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
        cust_row = cursor.fetchone()
        if not cust_row:
            raise ValueError("Could not find customer 'Perez and Sons' in the database.")
        customer_id = cust_row[0]
        
        # 2. Fetch Employee ID
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
        emp_row = cursor.fetchone()
        if not emp_row:
            raise ValueError("Could not find employee 'Miranda Harris' in the database.")
        employee_id = emp_row[0]
        
        # 3. Fetch 5 least expensive product IDs
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
        product_ids = [row[0] for row in cursor.fetchall()]
        
        # 4. Insert Order Record via RETURNING
        insert_order_query = """
            INSERT INTO orders (customer_id, employee_id) 
            VALUES (?, ?) 
            RETURNING order_id;
        """
        cursor.execute(insert_order_query, (customer_id, employee_id))
        new_order_id = cursor.fetchone()[0]
        
        # 5. Insert Line Items
        insert_li_query = """
            INSERT INTO line_items (order_id, product_id, quantity) 
            VALUES (?, ?, ?);
        """
        for prod_id in product_ids:
            cursor.execute(insert_li_query, (new_order_id, prod_id, 10))
            
        # Commit all inserts safely
        conn.commit()
        print(f"Successfully created Order ID {new_order_id} for Perez and Sons.")
        
        # 6. Verification SELECT query

        verify_query = """
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?;
        
        cursor.execute(verify_query, (new_order_id,))
        verify_results = cursor.fetchall()
        
        print("\nVerification Results for New Order:")
        for row in verify_results:
            print(f"Line Item ID: {row[0]} | Quantity: {row[1]} | Product: {row[2]}")
            
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed and was rolled back. Error: {e}")
        
    print("\n")

    # Task 4: Aggregation with HAVING

    print("--- Task 4: Employees with More Than 5 Orders ---")
    
    task4_query = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5;
   
    
    cursor.execute(task4_query)
    task4_results = cursor.fetchall()
    
    for row in task4_results:
        print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Orders Placed: {row[3]}")
    print("\n")

    # Clean up and close connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()