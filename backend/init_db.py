"""
Initialize database with sample tables and data.
Run this once after database is created.
"""

from sqlalchemy import text
from db import engine


def init_database():
    """Create sample tables and insert data."""
    
    with engine.connect() as conn:
        # Drop existing tables (optional — remove if you want to preserve data)
        # conn.execute(text("DROP TABLE IF EXISTS orders CASCADE;"))
        # conn.execute(text("DROP TABLE IF EXISTS users CASCADE;"))
        
        # Create users table
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                signup_date DATE NOT NULL,
                city VARCHAR(50)
            );
        """))
        
        # Create orders table
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                product VARCHAR(100) NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                order_date DATE NOT NULL,
                status VARCHAR(20)
            );
        """))
        
        # Create products table
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category VARCHAR(50),
                price DECIMAL(10, 2) NOT NULL,
                stock INTEGER
            );
        """))
        
        # Insert sample users
        conn.execute(text("""
            INSERT INTO users (name, email, signup_date, city) VALUES
            ('Alice Johnson', 'alice@example.com', '2024-01-15', 'New York'),
            ('Bob Smith', 'bob@example.com', '2024-02-20', 'Los Angeles'),
            ('Carol White', 'carol@example.com', '2024-03-10', 'Chicago'),
            ('David Brown', 'david@example.com', '2024-04-05', 'Houston'),
            ('Eve Davis', 'eve@example.com', '2024-05-12', 'Phoenix')
            ON CONFLICT (email) DO NOTHING;
        """))
        
        # Insert sample products
        conn.execute(text("""
            INSERT INTO products (name, category, price, stock) VALUES
            ('Laptop', 'Electronics', 999.99, 15),
            ('Mouse', 'Electronics', 29.99, 50),
            ('Keyboard', 'Electronics', 79.99, 30),
            ('Monitor', 'Electronics', 299.99, 20),
            ('USB Cable', 'Accessories', 9.99, 100),
            ('Desk Chair', 'Furniture', 199.99, 25),
            ('Desk Lamp', 'Furniture', 49.99, 40)
            ON CONFLICT DO NOTHING;
        """))
        
        # Insert sample orders
        conn.execute(text("""
            INSERT INTO orders (user_id, product, amount, order_date, status) VALUES
            (1, 'Laptop', 999.99, '2024-06-01', 'completed'),
            (1, 'Mouse', 29.99, '2024-06-05', 'completed'),
            (2, 'Keyboard', 79.99, '2024-06-10', 'pending'),
            (2, 'Monitor', 299.99, '2024-06-12', 'completed'),
            (3, 'Desk Chair', 199.99, '2024-06-15', 'completed'),
            (4, 'USB Cable', 9.99, '2024-06-18', 'completed'),
            (5, 'Desk Lamp', 49.99, '2024-06-20', 'pending'),
            (5, 'Keyboard', 79.99, '2024-06-22', 'completed'),
            (1, 'Monitor', 299.99, '2024-06-25', 'pending')
            ON CONFLICT DO NOTHING;
        """))
        
        conn.commit()
        print("✅ Database initialized with sample data!")


if __name__ == "__main__":
    init_database()
