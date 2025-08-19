import csv

file_path = "products_updated.csv"
new_file_path = "product_updated2.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        fieldnames = csv_reader.fieldnames + ["practice"]

        with open(new_file_path, mode="w", newline="", encoding="utf-8") as updated_file:
                csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
                csv_writer.writeheader()

                for row in csv_reader:
                        row["practice"] = "1 month"
                        csv_writer.writerow(row)