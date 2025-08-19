import csv

with open("products_updated.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

"""new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'MarcaX',
    'category': 'accesorios',
    'entry_date': '2023-10-15',
    'total_value': 7500.0
}

with open("products_updated.csv", mode="a", encoding="utf-8", newline="") as file:
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)"""