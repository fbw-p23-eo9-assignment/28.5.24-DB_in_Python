# DATABASE Usage in Python - 1 


## Exercise: Analyzing Sales Data
**Scenario:**
You're analyzing sales data for a retail company. You need to set up a database and perform various queries to extract insights from the data.

**Tasks:**

***SQL Queries in psql Terminal:***
- Create a PostgreSQL database named "sales_db".
- Create a table named "sales" with columns: id (serial, primary key), product_name (text), quantity_sold (integer), unit_price (numeric), and sale_date (date).
- Create a new user named "sales_analyst" with password "password" and grant SELECT privileges on the "sales" table to this user.

***Python Script:***
- Connect to the "sales_db" database using the "sales_analyst" user.
- Attempt to insert sample sales data into the "sales" table directly in the Python script.
Use the following sample data:
    - ('Laptop', 10, 1200.00, '2024-05-28')
    - ('Phone', 20, 800.00, '2024-05-29')
    - ('Tablet', 15, 500.00, '2024-05-29')
    - ('TV', 5, 1500.00, '2024-05-30')
    - ('Headphones', 30, 100.00, '2024-05-30')
- Check if you encountered an error specifying that *"the user doesn't have the INSERT privilege."*
- Go to the psql terminal and Grant ALL privilege to the "sales_analyst" user on the "sales" table.
- Perform the following queries in the python script using psycopg library:
    - Query 1: Try to insert the above mentioned data
    - Query 2: Retrieve all sales data.
    - Query 3: Calculate the total revenue generated from sales.
    - Query 4: Find the top 5 best-selling products by the quantity sold.
    - Query 5: Retrieve sales data for a specific date (e.g., '2024-05-28').

***Verification:***
- After running the Python script, verify the output matches the expected results.
- Delete the "sales_analyst" user from the psql terminal.