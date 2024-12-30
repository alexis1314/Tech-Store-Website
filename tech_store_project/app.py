from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for products (replace with a database in a real application)
products = [
    {"id": 1, "name": "Smartphone A", "price": 599.99, "description": "Latest smartphone with amazing features.", "image": "smartphone_a.jpg"},
    {"id": 2, "name": "Laptop B", "price": 999.99, "description": "Powerful laptop for work and play.", "image": "laptop_b.jpg"},
    {"id": 3, "name": "Wireless Headphones", "price": 199.99, "description": "Noise-cancelling over-ear headphones.", "image": "headphones.jpg"},
    {"id": 4, "name": "Smartwatch C", "price": 299.99, "description": "Smartwatch with health tracking.", "image": "smartwatch_c.jpg"}
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        customer_name = request.form['name']
        customer_email = request.form['email']
        selected_product = request.form['product']
        return render_template('thank_you.html', name=customer_name, product=selected_product)
    return render_template('checkout.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
