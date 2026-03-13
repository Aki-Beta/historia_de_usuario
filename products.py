products = []

def add_product(name, price, quantity):
    product = {
        'Product name': name,
        'Price': price,
        'Quantity': quantity
    }
    products.append(product)

def question():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    add_product(name, price, quantity)
    
    continuar = input("Do you want to add another product? (yes/no): ").strip().lower()
    if continuar == "yes":
        question()

def review_sales():
    print("===================")
    print("Daily sales report")
    total = 0
    for product in products:
        total_sales = product['Price'] * product['Quantity']
        total += total_sales
        print(f" Product name: {product['Product name']}")
        print(f" Total quantity sold: {product['Quantity']}")
    print(f" Total revenue: ${total: }")
    print("===================")