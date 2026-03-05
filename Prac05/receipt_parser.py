import re
import json

# read receipt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# 1. Extract prices
price_pattern = r"\d[\d\s]*,\d{2}"
prices = re.findall(price_pattern, text)

# convert prices to float
prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]


# 2. Extract product names
product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text)


# 3. Calculate total
total_calculated = sum(prices_clean)


# 4. Extract date and time
datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime = re.search(datetime_pattern, text)
datetime = datetime.group() if datetime else None


# 5. Extract payment method
payment_pattern = r"(Банковская карта|Наличные)"
payment_method = re.search(payment_pattern, text)
payment_method = payment_method.group() if payment_method else None


# 6. Structured output
result = {
    "products": products,
    "prices": prices_clean,
    "calculated_total": total_calculated,
    "payment_method": payment_method,
    "datetime": datetime
}

print(json.dumps(result, indent=4, ensure_ascii=False))