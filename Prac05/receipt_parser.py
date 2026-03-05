import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()


# product name + total price
pattern = r"\d+\.\s*\n(.+?)\n.*?\n([\d\s]+,\d{2})"

matches = re.findall(pattern, text, re.DOTALL)

products = []

for name, total in matches:
    price = float(total.replace(" ", "").replace(",", "."))
    
    products.append({
        "name": name.strip(),
        "total_price": price
    })


# calculate total
calculated_total = sum(p["total_price"] for p in products)


# datetime
datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)
datetime = datetime_match.group() if datetime_match else None


# payment method
payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group() if payment_match else None


result = {
    "products": products,
    "calculated_total": calculated_total,
    "payment_method": payment_method,
    "datetime": datetime
}

print(json.dumps(result, indent=4, ensure_ascii=False))