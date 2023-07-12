products = []

def add_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity of available items: "))
    product = {'name': name, 'description': description, 'price': price, 'quantity': quantity}
    products.append(product)
    print("Customer added.")

def update_product():
    name = input("Enter customer name to update: ")
    for product in products:
        if(product['name'] == name):
            description = input(f"Enter new description [Current: {product['description']}]: ")
            price = float(input(f"Enter new price [Current: {product['price']}]: "))
            quantity = int(input(f"Enter new quantity [Current: {product['quantity']}]: "))
            product['description'] = description
            product['price'] = price
            product['quantity'] = quantity
            print("Product updated.")
            return 
    print("Product not found")

def search_product():
    option = int(input("Search by:\n1. Name\n2. Price\n3. Quantity\nEnter option: "))
    if option == 1:
        name = input("Enter product name to search: ")
        filtered_products = list(filter(lambda product: name.lower() in product['name'].lower(), products))
    elif option == 2:
        price = float(input("Enter product price to search: "))
        filtered_products = list(filter(lambda product: price in product['price'], products))
    elif option == 3:
        quantity = int(input("Enter product quantity to search: "))
        filtered_products = list(filter(lambda product: quantity in product['quantity'], products))
    else:
        print("Invalid option.")
        return
    
    if len(filtered_products) > 0:
        print('Search results: ')
        print(f"Products found: {filtered_products}")
    else:
        print("No products found.")

def sort_products():
    option = int(input("Sort by:\n1. Name\n2. Price\n3. Quantity\nEnter option: "))
    if option == 1:
        sorted_products = sorted(products, key = lambda product: product['name'])
    elif option == 2:
        sorted_products = sorted(products, key = lambda product: product['price'])
    elif option == 3:
        sorted_products = sorted(products, key = lambda product: product['quantity'])
    else:
        print("Invalid option.")
        return
    
    print("Sorted products: ")
    print(sorted_products)

def change_quantity():
    name = input("Enter product name: ")
    filtered_products = list(filter(lambda product: name.lower() in product['name'].lower(), products))

    if len(filtered_products) > 0:
        product = filtered_products[0]
        addQuantity = int(input(f"How many to add? (Use negative numbers to decrease) [Current: {product['quantity']}]: "))
        product['quantity'] += addQuantity
        print(f"Added {addQuantity} to quantity!")
    else:
        print("Requested product was not found.")

def clear_inventory():
    products.clear()
    print("Inventory cleared")

def show_all():
    if len(products) > 0:
        for item in products:
            print(f'Name: {item["name"]}, Price:  {item["price"]}, Quantity: {item["quantity"]} (Description: {item["description"]})')
    else:
        print("Inventory is")
 
def inventory_main():
    while True:
        print("-- Product Management System --")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Search Product")
        print("4. Sort Products")
        print("5. Change Quantity")
        print("6. Clear Inventory")
        print("7. Show all products")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_product()
        elif choice == 2:
            update_product()
        elif choice == 3:
            search_product()
        elif choice == 4:
            sort_products()
        elif choice == 5:
            change_quantity()
        elif choice == 6:
            clear_inventory()
        elif choice == 7:
            show_all()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

inventory_main()

