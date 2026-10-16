from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import sqlite3
import uuid

DB_PATH = Path(__file__).with_name("orders.db")


@dataclass(frozen=True)
class Product:
    name: str
    price: float


PRODUCTS = {
    "innovative ladder": Product("Innovative Ladder", 1500.0),
    "multipurpose axe": Product("Multipurpose Axe", 1500.0),
    "smokeless bukhari": Product("Smokeless Bukhari", 10000.0),
    "walnut cracker": Product("Walnut Cracker", 50000.0),
}


class OrderDatabase:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _initialize(self):
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS orders (
                    order_id TEXT PRIMARY KEY,
                    customer_name TEXT NOT NULL,
                    product TEXT NOT NULL,
                    quantity INTEGER NOT NULL CHECK(quantity > 0),
                    unit_price REAL NOT NULL,
                    total REAL NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

    def save_order(self, customer_name, product, quantity):
        order_id = f"RI-{uuid.uuid4().hex[:8].upper()}"
        unit_price = product.price
        total = unit_price * quantity
        created_at = datetime.now().isoformat(timespec="seconds")
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO orders
                (order_id, customer_name, product, quantity, unit_price, total, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (order_id, customer_name, product.name, quantity, unit_price, total, created_at),
            )
        return order_id, total, created_at

    def recent_orders(self, limit=10):
        with self._connect() as conn:
            return conn.execute(
                """
                SELECT order_id, customer_name, product, quantity, unit_price, total, created_at
                FROM orders
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()


def find_product(name: str):
    return PRODUCTS.get(name.strip().casefold())


def ask_positive_integer(prompt: str):
    while True:
        value = input(prompt).strip()
        try:
            quantity = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
        return quantity


def show_products():
    print("\nAvailable products")
    print("-" * 42)
    for product in PRODUCTS.values():
        print(f"{product.name:<25} ₹{product.price:,.2f}")
    print("-" * 42)


def place_order(database: OrderDatabase):
    print("\n--- New Order ---")
    customer_name = input("Customer name: ").strip()
    if not customer_name:
        print("Customer name cannot be empty.")
        return

    show_products()
    product = None
    while product is None:
        product = find_product(input("Product: "))
        if product is None:
            print("Product not found. Please choose a product from the list.")

    quantity = ask_positive_integer("Quantity: ")
    order_id, total, created_at = database.save_order(customer_name, product, quantity)

    print("\nOrder saved successfully")
    print(f"Order ID : {order_id}")
    print(f"Customer : {customer_name}")
    print(f"Product  : {product.name}")
    print(f"Quantity : {quantity}")
    print(f"Total    : ₹{total:,.2f}")
    print(f"Created  : {created_at}")


def show_recent_orders(database: OrderDatabase):
    rows = database.recent_orders()
    if not rows:
        print("\nNo orders have been recorded yet.")
        return

    print("\n--- Recent Orders ---")
    for order_id, customer, product, quantity, unit_price, total, created_at in rows:
        print(f"{order_id} | {customer} | {product} x{quantity} | ₹{total:,.2f} | {created_at}")


def main():
    database = OrderDatabase()
    print("=" * 50)
    print("RAFIQ INNOVATIONS — ORDER MANAGEMENT")
    print("=" * 50)

    while True:
        print("\n1. View products")
        print("2. Place order")
        print("3. View recent orders")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_products()
        elif choice == "2":
            place_order(database)
        elif choice == "3":
            show_recent_orders(database)
        elif choice == "4":
            print("Thank you for using Rafiq Innovations Order Management.")
            break
        else:
            print("Invalid option. Choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
