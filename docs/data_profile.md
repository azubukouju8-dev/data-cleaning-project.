# Data profile — before and after cleaning

_Generated automatically by `notebooks/data_cleaning.ipynb`._

| | Raw | Clean |
|---|---|---|
| Orders rows | 473 | 450 |
| Products rows | 13 | 12 |
| Review lines / rows | 206 | 180 |

## Orders — before

| column         | dtype   |   missing |   missing_% |   unique | examples                                                                                                    |
|:---------------|:--------|----------:|------------:|---------:|:------------------------------------------------------------------------------------------------------------|
| order_id       | str     |         0 |         0   |      450 | ORD-1379, ORD-1230, ORD-1322, ORD-1251                                                                      |
| order_date     | str     |        22 |         4.7 |      350 | 2026-09-07, 2026-07-31, 09-08-2026, 04-12-2026                                                              |
| customer_id    | str     |         0 |         0   |       60 | C053, C035, C027, C038                                                                                      |
| customer_name  | str     |        14 |         3   |      163 | TUNDE GARCIA,   Ahmed Garcia , ?, Ahmed Brown                                                               |
| email          | str     |        28 |         5.9 |       77 | tunde.garcia53@example.com, ahmed.garcia35@example.com, zara.rossi27@example.com, ahmed.brown38@example.com |
| country        | str     |        13 |         2.7 |       29 | ghana, Ghana, -, UK                                                                                         |
| product_id     | str     |         0 |         0   |       15 | P001, P008, P009, P010                                                                                      |
| quantity       | str     |         0 |         0   |       11 | 4, 1, 3, 2                                                                                                  |
| unit_price     | str     |         0 |         0   |       24 | 25.99, 59.99, 29.9, 6.5                                                                                     |
| total          | str     |         0 |         0   |       87 | 10.4, 59.99, 119.6, 6.5                                                                                     |
| payment_method | str     |        25 |         5.3 |       24 | COD, paypal, CC, credit card                                                                                |
| status         | str     |         0 |         0   |       13 | Delivered, delivered, Delivered , Returned                                                                  |

## Orders — after

| column          | dtype          |   missing |   missing_% |   unique | examples                                                                                                     |
|:----------------|:---------------|----------:|------------:|---------:|:-------------------------------------------------------------------------------------------------------------|
| order_id        | str            |         0 |         0   |      450 | ORD-1001, ORD-1002, ORD-1003, ORD-1004                                                                       |
| order_date      | datetime64[us] |        36 |         8   |      222 | 2026-10-04, 2026-08-18, 2026-08-21, 2026-10-19                                                               |
| customer_id     | str            |         0 |         0   |       60 | C018, C016, C025, C056                                                                                       |
| customer_name   | str            |        13 |         2.9 |       52 | Ngozi Nwosu, Zara Tanaka, Emeka Okafor, Ahmed Garcia                                                         |
| email           | str            |        39 |         8.7 |       60 | ngozi.nwosu18@example.com, zara.tanaka16@example.com, emeka.okafor25@example.com, ahmed.garcia56@example.com |
| country         | str            |        12 |         2.7 |        6 | Nigeria, United Kingdom, South Africa, Kenya                                                                 |
| product_id      | str            |         0 |         0   |       13 | P011, P004, P005, P002                                                                                       |
| quantity        | Int64          |        17 |         3.8 |        5 | 1, 4, 2, 3                                                                                                   |
| unit_price      | float64        |         0 |         0   |       12 | 99.0, 34.0, 149.0, 79.5                                                                                      |
| total           | float64        |        17 |         3.8 |       59 | 99.0, 34.0, 596.0, 159.0                                                                                     |
| total_reported  | float64        |         0 |         0   |       87 | 99.0, 34.0, 685.4, 159.0                                                                                     |
| payment_method  | str            |        24 |         5.3 |        4 | Mobile Wallet, Bank Transfer, Card, Cash on Delivery                                                         |
| status          | str            |         0 |         0   |        4 | Shipped, Delivered, Returned, Cancelled                                                                      |
| quantity_flag   | str            |       433 |        96.2 |        2 | , invalid (<=0 or >50)                                                                                       |
| total_corrected | bool           |         0 |         0   |        2 | False, True                                                                                                  |
| unknown_product | bool           |         0 |         0   |        2 | False, True                                                                                                  |

## Products — before

| column         | dtype   |   missing |   missing_% |   unique | examples                                                          |
|:---------------|:--------|----------:|------------:|---------:|:------------------------------------------------------------------|
| product_id     | str     |         0 |         0   |       12 | P001, P002, P003, P004                                            |
| name           | str     |         0 |         0   |       12 | Wireless Mouse, Mechanical Keyboard, USB-C Cable 1m, Laptop Stand |
| category       | str     |         1 |         7.7 |        9 | Electronics, Accessories, Accesories, ELECTRONICS                 |
| price          | object  |         1 |         7.7 |       12 | $25.99, 79.5, 9.99, 34.0                                          |
| in_stock       | object  |         0 |         0   |        5 | True, 0, False, yes                                               |
| specs.weight_g | object  |         2 |        15.4 |        7 | 1146, 2253, 915, unknown                                          |
| specs.color    | str     |         2 |        15.4 |        5 | Black, gray, grey, black                                          |

## Products — after

| column     | dtype   |   missing |   missing_% |   unique | examples                                                          |
|:-----------|:--------|----------:|------------:|---------:|:------------------------------------------------------------------|
| product_id | str     |         0 |         0   |       12 | P001, P002, P003, P004                                            |
| name       | str     |         0 |         0   |       12 | Wireless Mouse, Mechanical Keyboard, USB-C Cable 1m, Laptop Stand |
| category   | str     |         0 |         0   |        4 | Electronics, Accessories, Stationery, Home Office                 |
| price      | float64 |         0 |         0   |       12 | 25.99, 79.5, 9.99, 34.0                                           |
| in_stock   | bool    |         0 |         0   |        2 | True, False                                                       |
| weight_g   | float64 |         6 |        50   |        6 | 1146.0, 2253.0, 915.0, 1398.0                                     |
| color      | str     |         2 |        16.7 |        3 | black, grey, white                                                |

## Reviews — after

| column      | dtype          |   missing |   missing_% |   unique | examples                                                                          |
|:------------|:---------------|----------:|------------:|---------:|:----------------------------------------------------------------------------------|
| review_date | datetime64[us] |         0 |         0   |      134 | 2026-08-15, 2026-05-21, 2026-04-22, 2026-06-04                                    |
| order_id    | str            |         5 |         2.8 |      149 | ORD-1233, ORD-1140, ORD-1080, ORD-1195                                            |
| rating      | Int64          |         2 |         1.1 |        5 | 1, 3, 4, 5                                                                        |
| comment     | str            |         0 |         0   |       16 | Waste of money, It's okay., Nice, but delivery took long., Great value for money. |
| order_found | bool           |         0 |         0   |        2 | True, False                                                                       |

