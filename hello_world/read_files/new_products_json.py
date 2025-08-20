import json

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'MarcaX',
    'category': 'accesorios',
    'entry_date': '2023-10-15',
}

file_path = "products.json"
new_file_path = "products_updated.json"

with open(file_path, mode="r", encoding="utf-8") as file:
    products = json.load(file)

products.append(new_product)

with open(new_file_path, mode="w", encoding="utf-8") as file:
    json.dump(products, file, indent=4)