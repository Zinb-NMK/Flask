import mysql.connector

# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'database': 'ecommerce'
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create the products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    description TEXT
)
""")

# Insert sample data into the table
cursor.executemany("""
INSERT INTO products (name, price, description)
VALUES (%s, %s, %s)
""", [
    ('Product A', 100.0, 'Description for Product A'),
    ('Product B', 200.0, 'Description for Product B'),
    ('Product C', 300.0, 'Description for Product C')
])

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Database setup complete!")
