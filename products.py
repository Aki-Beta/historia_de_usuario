products = []
    
# This module contains the functions to manage the products and sales records for a store.
def add_product(products):

    product_name = input("Product name: ")

    next = True
    while next:
        try: 
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            break

        except ValueError:
            print("invalid imput. please enter numeric value. ")
            
        
    product = {
        'Product name': product_name,
        'Price': price,
        'Quantity': quantity
    }

    products.append(product)
    

# This function generates a sales report based on the products added to the sales record.
def review_sales():

    products = []
    next = "yes"

    while next == "yes":
        add_product(products)
        next = input("Do you want to add another product? (yes/no): ").strip().lower()
        
        
    print("===================")
    print("Daily sales report")

    total = 0

    for product in products:
            
        total_sales = product['Price'] * product['Quantity']
        total += total_sales

        print(f" Product name: {product['Product name']}")
        print(f"Price: ${product['Price']:}")
        print(f"Total quantity sold: {product['Quantity']}")
        print(f"Subtotal: ${total_sales:}")

    print(f" Total revenue: ${total: }")
    
    print("===================")