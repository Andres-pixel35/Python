import statistics
import csv

with open("month_sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    monthly_sales = {}
    for row in reader:
        month = row["month"]
        sales = int(row["sales"])

        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

average_sales = statistics.mean(sales)

print(average_sales)

median_sale = statistics.median(sales)
print(median_sale)

mode_sale = statistics.mode(sales)
print(mode_sale)

stdev_sales = statistics.stdev(sales)
print(stdev_sales)

variance_sales = statistics.variance(sales)
print(variance_sales)

max_sales = max(sales)
min_sales = min(sales)

print(max_sales)
print(min_sales)