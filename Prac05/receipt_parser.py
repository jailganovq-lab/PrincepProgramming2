import re
import json

# read receipt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# 1. Extract prices (only correct money format)
price_pattern = r"\d{1,3}(?: \d{3})*,\d{2}"
prices = re.findall(price_pattern, text)

# convert prices to float
prices_clean = []
for p in prices:
    clean = p.replace(" ", "").replace(",", ".")
    try:
        prices_clean.append(float(clean))
    except ValueError:
        pass


# 2. Extract product names
product_pattern = r"\d+\.\s*\n(.+)"
products = re.findall(product_pattern, text)


# 3. Calculate total
total_calculated = sum(prices_clean)


# 4. Extract date and time
datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)
datetime = datetime_match.group() if datetime_match else None


# 5. Extract payment method
payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group() if payment_match else None


# 6. Structured output
result = {
    "products": products,
    "prices": prices_clean,
    "calculated_total": total_calculated,
    "payment_method": payment_method,
    "datetime": datetime
}

print(json.dumps(result, indent=4, ensure_ascii=False))