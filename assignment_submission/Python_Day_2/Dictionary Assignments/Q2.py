products = {
    "soap": 100,
    "deo": 300,
    "perfume": 400
}

user_input = input("Enter product name: ").lower()

if user_input in products:
    print("Price:", products[user_input])
else:
    print("Product not available")