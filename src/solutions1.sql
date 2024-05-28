-- Create database
CREATE DATABASE sales_db;

-- Connect to database
\c sales_db

-- Create sales table
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_name TEXT,
    quantity_sold INTEGER,
    unit_price NUMERIC,
    sale_date DATE
);

-- Create user and grant privileges
CREATE USER sales_analyst WITH PASSWORD 'password';
GRANT SELECT ON sales TO sales_analyst;
