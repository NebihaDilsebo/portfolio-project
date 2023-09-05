#!/usr/bin/python3
"""consol"""

from website import create_app, db
from website.models import Product

app = create_app()

def add_product():
    print("Add a New Product")
    name = input("Product Name: ")
    description = input("Product Description: ")
    price = float(input("Product Price: "))

    product = Product(name=name, description=description, price=price)
    db.session.add(product)
    db.session.commit()
    print("Product added successfully!\n")

def view_products():
    print("List of Products")
    products = Product.query.all()
    if products:
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price:.2f}")
    else:
        print("No products found.\n")

def main_menu():
    while True:
        print("Fashion Website Console")
        print("1. Add Product")
        print("2. View Products")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    main_menu()

