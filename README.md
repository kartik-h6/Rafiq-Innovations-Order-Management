# Rafiq Innovations — Order Management System

A lightweight Python + SQLite order-management application inspired by the product workflow of **Rafiq Innovations Pvt Ltd**.

## What it demonstrates

- Product catalogue with prices
- Case-insensitive product lookup
- Customer and quantity validation
- Unique order IDs
- Automatic order totals
- Persistent SQLite storage
- Recent-order history
- Parameterized SQL queries
- Separation between application logic and database operations

## Product catalogue

| Product | Price |
|---|---:|
| Innovative Ladder | ₹1,500 |
| Multipurpose Axe | ₹1,500 |
| Smokeless Bukhari | ₹10,000 |
| Walnut Cracker | ₹50,000 |

## Run locally

Requires Python 3.9+.

```bash
python main.py
```

No third-party packages are required.

## Workflow

```text
View products → Place order → Save to SQLite → View recent orders
```

The database file `orders.db` is created automatically when the application starts.

## Roadmap

- [ ] Customer records and customer order history
- [ ] Inventory and low-stock tracking
- [ ] Order status workflow
- [ ] PDF quotation/invoice generation
- [ ] CSV/Excel export
- [ ] Desktop GUI
- [ ] Web dashboard

## Note

This is a portfolio/learning project. Product prices are sample values and the application is not connected to a live company inventory or sales system.

## Author

**Mahid Rafiq**

- GitHub: https://github.com/mahidrafiq
- LinkedIn: https://www.linkedin.com/in/mahidrafiq
