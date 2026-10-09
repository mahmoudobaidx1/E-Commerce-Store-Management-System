# E-Commerce & Store Management System

A Python-based command-line store management system integrated with SQLite (`store.db`). This project provides functionalities for both store administrators to manage inventory and customers to search, add products to a shopping cart, modify cart items, and complete checkout.

---

## 📁 Project Structure

* **`admin.py`**: Contains the `Admin` class allowing store administrators to add new products (name, price, quantity) into the database.
* **`search.py`**: Contains the `Search` class for searching products by name and adding requested quantities directly to the shopping cart.
* **`home_page.py`**: Contains the `home_page` class to display all available store products and allow users to add items to their cart.
* **`cart.py`**: Contains the `Cart` class to display active cart items, modify quantities, remove items, and process final purchase checkouts while automatically updating inventory stock.
* **`store.db`**: SQLite database storing table records for `products` and `cart`.

---

## ✨ Features

* **Admin Operations:** Easily insert new inventory items with cleaned inputs (lowercase and trimmed spaces).
* **Product Search:** Instantly look up product availability, pricing, and stock status.
* **Shopping Cart Management:** View cart contents, update item quantities, remove items, or proceed to checkout.
* **Automatic Inventory Sync:** Updating or completing a purchase automatically updates remaining product stock in `store.db`.

---

## 🚀 How to Run

1. **Clone or Download the Repository:**
   Ensure all `.py` files and `store.db` are placed in the same directory.

2. **Prerequisites:**
   Python 3.x installed (no external libraries needed as standard `sqlite3` is used).

3. **Execution Options:**
   * To add new products as an admin:
     ```bash
     python admin.py
     ```
   * To browse products and add to cart:
     ```bash
     python home_page.py
     ```
   * To search for specific items:
     ```bash
     python search.py
     ```
   * To view and manage your cart / checkout:
     ```bash
     python cart.py
     ```