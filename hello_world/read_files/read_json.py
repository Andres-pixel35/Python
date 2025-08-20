import json

with open('products.json', mode='r', encoding='utf-8') as file:
    products = json.load(file)
    for product in products:
        print(f'Product: {product['name']} | Price: {product['price']}')