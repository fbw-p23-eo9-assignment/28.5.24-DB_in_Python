import psycopg2
from psycopg2 import sql, Error

# Connect to PostgreSQL as sales_analyst user
conn = psycopg2.connect(
    dbname="sales_db",
    user="sales_analyst",
    password="password",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()
print("Cursor output : ", cur)
print("Connection details : ", conn.get_dsn_parameters())
# Attempt to insert sample sales data into the "sales" table
sales_data = [
    ('Laptop', 10, 1200.00, '2024-05-28'),
    ('Phone', 20, 800.00, '2024-05-29'),
    ('Tablet', 15, 500.00, '2024-05-29'),
    ('TV', 5, 1500.00, '2024-05-30'),
    ('Headphones', 30, 100.00, '2024-05-30')
]

# Grant INSERT privilege to the "sales_analyst" user on the "sales" table on the psql terminal 
# GRANT all privileges on table sales to sales_analyst;


#GRant sequence usage to the user in terminal :
# grant usage, select on sequence sales_id_seq to sales_analyst;


# Query 1: Insert into sales table: 
insert_query = """
    INSERT INTO sales (product_name, quantity_sold, unit_price, sale_date)
    VALUES (%s, %s, %s, %s);
"""
try:
    cur.executemany(insert_query, sales_data)
    conn.commit()
    print("Query 1: Sample sales data inserted successfully!")
except Error as e:
    print("Error:", e)

# Query 2: Retrieve all sales data
cur.execute("""
    SELECT * FROM sales;
""")
rows = cur.fetchall()
print("\nQuery 2: All Sales Data")
for row in rows:
    print(row)

# # Query 3: Calculate total revenue generated from sales
cur.execute("""
    SELECT SUM(quantity_sold * unit_price) AS total_revenue FROM sales;
""")
total_revenue = cur.fetchone()[0]
print("\nQuery 3: Total Revenue")
print("Total Revenue:", total_revenue)

# # Query 4: Find top 5 best-selling products by quantity sold
cur.execute("""
    SELECT product_name, SUM(quantity_sold) AS total_sold 
    FROM sales 
    GROUP BY product_name 
    ORDER BY total_sold DESC 
    LIMIT 5;
""")
top_products = cur.fetchall()
print("\nQuery 4: Top 5 Best-Selling Products")
for product in top_products:
    print(product)

# Query 5: Retrieve sales data for a specific date
cur.execute("""
    SELECT * FROM sales 
    WHERE sale_date = '2024-05-28';
""")
sales_on_date = cur.fetchall()
print("\nQuery 5: Sales on 2024-05-28")
for sale in sales_on_date:
    print(sale)

# Close the cursor and connection
cur.close()
conn.close()
