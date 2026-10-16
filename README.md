# Rafiq Innovations — Order Management System

> A portfolio-grade order management application built with **Python + SQLite**, with an interactive static web demo published through GitHub Pages.

## 🌐 Web Demo

**GitHub Pages:** `https://mahidrafiq.github.io/Rafiq-Innovations-Order-Management/`

The Pages version is a browser-based demonstration of the core workflow. It does not run the Python/SQLite backend in the browser.

## What it demonstrates

- Product catalogue with prices
- Case-insensitive product lookup
- Customer and quantity validation
- Unique order IDs
- Automatic order totals
- Persistent SQLite storage in the Python application
- Recent-order history
- Parameterized SQL queries
- Separation between application logic and database operations
- Interactive browser demo for recruiters and visitors

## Product catalogue

| Product | Price |
|---|---:|
| Innovative Ladder | ₹1,500 |
| Multipurpose Axe | ₹1,500 |
| Smokeless Bukhari | ₹10,000 |
| Walnut Cracker | ₹50,000 |

## Project structure

```text
.
├── main.py
├── README.md
├── docs/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── .github/
    └── workflows/
        └── pages.yml
```

## Run the Python application locally

Requires Python 3.9+.

```bash
python main.py
```

No third-party packages are required.

The database file `orders.db` is created automatically when the application starts.

## GitHub Pages deployment

The `pages.yml` workflow deploys the contents of `/docs` whenever changes are pushed to `main`. GitHub Pages must be configured to use **GitHub Actions** as its publishing source.

## Workflow

```text
View products → Place order → Validate → Save to SQLite → View recent orders
```

## Roadmap

- [ ] Customer records and customer order history
- [ ] Inventory and low-stock tracking
- [ ] Order status workflow
- [ ] PDF quotation/invoice generation
- [ ] CSV/Excel export
- [ ] Desktop GUI
- [ ] Web dashboard connected to a backend API

## Note

This is a portfolio/learning project. Product prices are sample values and the application is not connected to a live company inventory or sales system.

## Author

**Mahid Rafiq**

- GitHub: https://github.com/mahidrafiq
- LinkedIn: https://www.linkedin.com/in/mahidrafiq
