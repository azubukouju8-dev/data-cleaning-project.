# Data dictionary (cleaned data)

## `data/cleaned/orders_clean.csv` — one row per order (450 rows)

| Column | Type | Description | Allowed values / notes |
|---|---|---|---|
| order_id | text | Unique order ID | `ORD-####`, unique |
| order_date | date | Order date | `YYYY-MM-DD`; missing if unknown/invalid |
| customer_id | text | Customer ID | `C###` |
| customer_name | text | Customer full name | Title Case; may be missing |
| email | text | Customer email | Lowercase, valid format; may be missing |
| country | text | Customer country | Nigeria, Ghana, Kenya, United Kingdom, United States, South Africa |
| product_id | text | Product ID (links to products) | `P###` |
| quantity | integer | Units ordered | 1–50; missing if invalid |
| unit_price | decimal (USD) | Price per unit | > 0 |
| total | decimal (USD) | quantity × unit_price (recomputed) | Missing if quantity missing |
| total_reported | decimal (USD) | Total as in the raw file | Kept for audit |
| payment_method | text | How the customer paid | Card, Bank Transfer, Cash on Delivery, Mobile Wallet |
| status | text | Order status | Delivered, Shipped, Cancelled, Returned |
| quantity_flag | text | Why quantity was removed | Empty or `invalid (<=0 or >50)` |
| total_corrected | boolean | Reported total differed from recomputed | True/False |
| unknown_product | boolean | product_id not in catalogue | True/False |

## `data/cleaned/products_clean.csv` — one row per product (12 rows)

| Column | Type | Description |
|---|---|---|
| product_id | text | Unique product ID `P###` |
| name | text | Product name |
| category | text | Electronics, Accessories, Stationery, Home Office |
| price | decimal (USD) | List price |
| in_stock | boolean | Available to order |
| weight_g | number | Weight in grams; missing if unknown |
| color | text | Lowercase colour; `grey` spelling |

## `data/cleaned/reviews_clean.csv` — one row per review

| Column | Type | Description |
|---|---|---|
| review_date | date | `YYYY-MM-DD` |
| order_id | text | Reviewed order (links to orders); may be missing |
| rating | integer | 1–5; missing if unreadable or wrong scale |
| comment | text | Review text, trimmed |
| order_found | boolean | order_id exists in orders_clean.csv |
