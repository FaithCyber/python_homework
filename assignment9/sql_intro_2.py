import sqlite3
import pandas as pd

# =========================
# Task 5: Read Data into a DataFrame
# =========================

try:
    # Connect to lesson database
    conn = sqlite3.connect("../db/lesson.db")

    # Load data using SQL JOIN
    query = """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products
    ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(query, conn)

    # Print first 5 rows
    print("\n--- Original DataFrame ---")
    print(df.head())

    # Add total column
    df['total'] = df['quantity'] * df['price']

    print("\n--- With Total Column ---")
    print(df.head())

    # Group by product_id
    grouped = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    }).reset_index()

    print("\n--- Grouped DataFrame ---")
    print(grouped.head())

    # Sort by product_name
    grouped = grouped.sort_values(by='product_name')

    print("\n--- Sorted DataFrame ---")
    print(grouped.head())

    # Save to CSV
    grouped.to_csv("order_summary.csv", index=False)

    print("\nFile 'order_summary.csv' created successfully.")

except sqlite3.Error as e:
    print("Database error:", e)

except Exception as e:
    print("Error:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")