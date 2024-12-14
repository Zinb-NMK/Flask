from flask import Flask, render_template, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests if needed

# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',       # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'database': 'ecommerce'
}

# Helper Function to Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Home Route
@app.route("/")
def index():
    return render_template("index.html")

# API Route: Fetch all products
@app.route("/products", methods=["GET"])
def get_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        conn.close()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Route: Fetch a specific product by ID
@app.route("/select_product/<int:product_id>", methods=["GET"])
def select_product(product_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        conn.close()
        if product:
            return jsonify(product)
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Route: Add a new product (Optional feature)
@app.route("/add_product", methods=["POST"])
def add_product():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)",
            (data["name"], data["price"], data["description"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Product added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
