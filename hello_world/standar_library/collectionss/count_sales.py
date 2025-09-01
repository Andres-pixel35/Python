from collections import Counter

def count_sales(products: list[str]) -> Counter:
    return Counter(products)

products = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet']
result = count_sales(products)
print(result) 
