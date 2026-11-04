"""
generate_raw_data.py

Creates a deliberately messy, SYNTHETIC dataset for data-cleaning practice:
  data/raw/orders.csv      - online store orders (CSV)
  data/raw/products.json   - product catalogue (JSON)
  data/raw/reviews.txt     - customer reviews (semi-structured text)

The files are linked by IDs (order_id, product_id).
A fixed random seed makes the output identical every time it runs.
Uses only the Python standard library.

Run from the project root:
    python generate_raw_data.py
"""

import csv
import json
import os
import random
from datetime import date, timedelta

SEED = 42
random.seed(SEED)

OUT_DIR = os.path.join("data", "raw")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. PRODUCTS (JSON)
# ---------------------------------------------------------------------------
product_base = [
    ("P001", "Wireless Mouse", "Electronics", 25.99),
    ("P002", "Mechanical Keyboard", "Electronics", 79.50),
    ("P003", "USB-C Cable 1m", "Accessories", 9.99),
    ("P004", "Laptop Stand", "Accessories", 34.00),
    ("P005", "Noise-Cancelling Headphones", "Electronics", 149.00),
    ("P006", "Notebook A5 (pack of 3)", "Stationery", 12.75),
    ("P007", "Desk Lamp LED", "Home Office", 42.00),
    ("P008", "Webcam 1080p", "Electronics", 59.99),
    ("P009", "Ergonomic Chair Cushion", "Home Office", 29.90),
    ("P010", "Ballpoint Pens (box of 12)", "Stationery", 6.50),
    ("P011", "External SSD 1TB", "Electronics", 99.00),
    ("P012", "Phone Holder", "Accessories", 14.25),
]

category_variants = {
    "Electronics": ["Electronics", "electronics", "ELECTRONICS", "Electronic"],
    "Accessories": ["Accessories", "accessories", "Accesories"],
    "Stationery": ["Stationery", "stationary", "Stationery "],
    "Home Office": ["Home Office", "home-office", "HomeOffice"],
}

products = []
for pid, name, cat, price in product_base:
    p = {
        "product_id": pid,
        "name": name,
        "category": random.choice(category_variants[cat]),
        "price": price,
        "in_stock": random.choice([True, False, "yes", "no", 1, 0]),
        "specs": {
            "weight_g": random.choice([random.randint(20, 2500), None, "unknown"]),
            "color": random.choice(["black", "Black", "white", "grey", "gray", None]),
        },
    }
    # Messy price formats
    r = random.random()
    if r < 0.25:
        p["price"] = f"${price:.2f}"
    elif r < 0.40:
        p["price"] = str(price)
    products.append(p)

# Missing fields
del products[5]["category"]
products[9]["price"] = None
# Duplicate product with a conflicting price
dup = json.loads(json.dumps(products[1]))
dup["price"] = 74.99
products.append(dup)
# Product id with whitespace / lowercase
products[10]["product_id"] = " p011"

catalogue = {
    "store": "Demo Electronics & Office Supplies (synthetic)",
    "exported_at": "2026-10-31T23:59:59",
    "currency": "USD",
    "products": products,
}

with open(os.path.join(OUT_DIR, "products.json"), "w", encoding="utf-8") as f:
    json.dump(catalogue, f, indent=2)

# ---------------------------------------------------------------------------
# 2. ORDERS (CSV)
# ---------------------------------------------------------------------------
first_names = ["Amara", "Tunde", "Chloe", "David", "Fatima", "Kwame", "Sofia",
               "Liam", "Ngozi", "Ahmed", "Grace", "Mateo", "Yuki", "Emeka", "Zara"]
last_names = ["Okafor", "Smith", "Bello", "Garcia", "Mensah", "Brown",
              "Ibrahim", "Nwosu", "Rossi", "Tanaka", "Adeyemi", "Khan"]

customers = []
for i in range(1, 61):
    fn, ln = random.choice(first_names), random.choice(last_names)
    customers.append({
        "customer_id": f"C{i:03d}",
        "name": f"{fn} {ln}",
        "email": f"{fn.lower()}.{ln.lower()}{i}@example.com",
        "country": random.choice(["Nigeria", "Ghana", "Kenya", "United Kingdom",
                                  "United States", "South Africa"]),
    })

country_variants = {
    "Nigeria": ["Nigeria", "nigeria", "NG", "Nigeria ", "NGA"],
    "Ghana": ["Ghana", "ghana", "GH"],
    "Kenya": ["Kenya", "KENYA", "KE"],
    "United Kingdom": ["United Kingdom", "UK", "U.K.", "England"],
    "United States": ["United States", "USA", "US", "U.S.A", "united states"],
    "South Africa": ["South Africa", "south africa", "ZA", "S. Africa"],
}
payment_variants = {
    "card": ["Card", "card", "credit card", "Credit Card", "CC", "debit card"],
    "transfer": ["Bank Transfer", "transfer", "bank transfer", "Transfer "],
    "cash": ["Cash", "cash on delivery", "COD", "CASH"],
    "wallet": ["Mobile Wallet", "wallet", "PayPal", "paypal"],
}
status_variants = {
    "delivered": ["Delivered", "delivered", "DELIVERED", "Delivered "],
    "shipped": ["Shipped", "shipped", "In transit"],
    "cancelled": ["Cancelled", "canceled", "CANCELLED"],
    "returned": ["Returned", "returned", "Refunded"],
}
missing_tokens = ["", "N/A", "null", "-", "NaN", "?"]

start = date(2026, 1, 1)


def messy_date(d):
    """Return the date in one of several inconsistent formats."""
    fmt = random.random()
    if fmt < 0.45:
        return d.strftime("%Y-%m-%d")
    if fmt < 0.65:
        return d.strftime("%d/%m/%Y")
    if fmt < 0.80:
        return d.strftime("%m-%d-%Y")
    if fmt < 0.90:
        return d.strftime("%B %d, %Y")
    if fmt < 0.95:
        return d.strftime("%d %b %Y")
    return d.strftime("%Y/%m/%d %H:%M")


def messy_name(n):
    r = random.random()
    if r < 0.10:
        return n.upper()
    if r < 0.20:
        return n.lower()
    if r < 0.30:
        return f"  {n} "
    return n


price_lookup = {pid: price for pid, _, _, price in product_base}

rows = []
for i in range(1, 451):
    c = random.choice(customers)
    pid = random.choice(list(price_lookup))
    qty = random.choices([1, 2, 3, 4, 5], weights=[50, 25, 12, 8, 5])[0]
    unit = price_lookup[pid]
    d = start + timedelta(days=random.randint(0, 300))

    row = {
        "order_id": f"ORD-{1000 + i}",
        "order_date": messy_date(d),
        "customer_id": c["customer_id"],
        "customer_name": messy_name(c["name"]),
        "email": c["email"],
        "country": random.choice(country_variants[c["country"]]),
        "product_id": pid,
        "quantity": qty,
        "unit_price": unit,
        "total": round(qty * unit, 2),
        "payment_method": random.choice(
            payment_variants[random.choice(list(payment_variants))]),
        "status": random.choice(status_variants[random.choices(
            list(status_variants), weights=[70, 15, 10, 5])[0]]),
    }

    # --- Inject problems ---
    r = random.random
    if r() < 0.12:
        row["unit_price"] = f"${unit:,.2f}"            # currency string
    if r() < 0.06:
        row["quantity"] = random.choice(["two", "1 ", "3pcs", "0", "-1"])
    if r() < 0.01:
        row["quantity"] = 999                          # outlier
    if r() < 0.07:
        row["total"] = round(row["total"] * random.choice([10, 0.1, 1.15]), 2)  # wrong total
    if r() < 0.06:
        row["email"] = random.choice(missing_tokens)
    if r() < 0.04:
        row["email"] = row["email"].replace("@", "") if "@" in str(row["email"]) else row["email"]
    if r() < 0.05:
        row["order_date"] = random.choice(missing_tokens)
    if r() < 0.02:
        row["order_date"] = "2027-02-30"               # impossible date
    if r() < 0.05:
        row["country"] = random.choice(missing_tokens)
    if r() < 0.04:
        row["payment_method"] = random.choice(missing_tokens)
    if r() < 0.03:
        row["product_id"] = random.choice(["P099", "p003", " P005"])  # unknown / bad format
    if r() < 0.03:
        row["customer_name"] = random.choice(missing_tokens)
    rows.append(row)

# Exact duplicates
for _ in range(15):
    rows.append(dict(random.choice(rows)))
# Near-duplicates (same order_id, slightly different data)
for _ in range(8):
    base = dict(random.choice(rows))
    base["customer_name"] = str(base["customer_name"]).strip().upper()
    base["status"] = random.choice(["Delivered", "Shipped"])
    rows.append(base)

random.shuffle(rows)

fieldnames = list(rows[0].keys())
with open(os.path.join(OUT_DIR, "orders.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# ---------------------------------------------------------------------------
# 3. REVIEWS (semi-structured text)
# ---------------------------------------------------------------------------
review_texts = {
    5: ["Excellent quality, arrived early!", "Love it. Works perfectly.",
        "Best purchase this year 🙌", "Great value for money."],
    4: ["Good product, packaging was a bit damaged.", "Works well, slightly overpriced.",
        "Nice, but delivery took long."],
    3: ["It's okay.", "Average quality, does the job.", "Not bad, not great."],
    2: ["Stopped working after two weeks.", "Colour was different from the picture."],
    1: ["Terrible. Never arrived on time and support ignored me.",
        "Broken on arrival!!!", "Waste of money"],
}
rating_formats = [
    lambda s: f"{s}/5",
    lambda s: f"{s} stars",
    lambda s: str(s),
    lambda s: ["", "one", "two", "three", "four", "five"][s],
    lambda s: "★" * s,
]
separators = [" | ", "|", " ; ", "\t", " - "]

valid_orders = [r for r in rows if str(r["order_id"]).startswith("ORD-")]
review_lines = ["# Customer reviews export (synthetic)",
                "# format: date | order_id | rating | comment", ""]
for _ in range(180):
    o = random.choice(valid_orders)
    stars = random.choices([5, 4, 3, 2, 1], weights=[35, 30, 15, 10, 10])[0]
    d = start + timedelta(days=random.randint(5, 305))
    date_str = messy_date(d) if random.random() < 0.3 else d.isoformat()
    oid = o["order_id"]
    if random.random() < 0.05:
        oid = oid.lower()
    if random.random() < 0.03:
        oid = ""
    rating = random.choice(rating_formats)(stars)
    if random.random() < 0.04:
        rating = random.choice(["", "N/A", "10/10"])
    comment = random.choice(review_texts[stars])
    if random.random() < 0.10:
        comment = "   " + comment.upper() + "   "
    sep = random.choice(separators) if random.random() < 0.25 else " | "
    line = sep.join([date_str, oid, rating, comment])
    review_lines.append(line)
    if random.random() < 0.05:
        review_lines.append(line)                       # duplicate line
    if random.random() < 0.04:
        review_lines.append("")                         # stray blank line
    if random.random() < 0.02:
        review_lines.append("ERROR: export timeout, retrying...")  # junk line

with open(os.path.join(OUT_DIR, "reviews.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(review_lines) + "\n")

print("Created:")
for fn in ["orders.csv", "products.json", "reviews.txt"]:
    path = os.path.join(OUT_DIR, fn)
    print(f"  {path}  ({os.path.getsize(path):,} bytes)")
