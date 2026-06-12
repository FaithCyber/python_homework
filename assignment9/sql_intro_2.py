import sqlite3
import pandas as pd

try:
    # Connect to lesson.db
    with sqlite3.connect("../db/lesson.db") as conn:

        sql_statement = """
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

        # Read SQL query into DataFrame
        df = pd.read_sql_query(sql_statement, conn)

        print("First 5 rows:")
        print(df.head())

        # Create total column
        df["total"] = df["quantity"] * df["price"]

        print("\nFirst 5 rows with total column:")
        print(df.head())

        # Group by product_id
        summary_df = df.groupby("product_id").agg({
            "line_item_id": "count",
            "total": "sum",
            "product_name": "first"
        })

        print("\nGrouped Data:")
        print(summary_df.head())

        # Sort by product_name
        summary_df = summary_df.sort_values("product_name")

        # Save CSV
        summary_df.to_csv("order_summary.csv")

        print("\norder_summary.csv created successfully!")

except Exception as e:
    print("Error:", e)

finally:
    print("Connection closed.")