# E-Cart - Dummy E-Commerce Project

A Python-based dummy e-commerce project demonstrating object-oriented programming with proper class methods and project structure.

## Project Structure

```
TTI_Testing/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── product.py           # Product class
│   ├── cart.py              # Shopping cart class
│   ├── user.py              # User class
│   ├── order.py             # Order class
│   └── store.py             # Store management class
├── main.py                  # Main application demo
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Features

### Core Classes

1. **Product** (`src/product.py`)
   - Product management with ID, name, price, description, and stock
   - Methods: `update_price()`, `update_stock()`, `is_available()`, `get_discount_price()`

2. **Cart** (`src/cart.py`)
   - Shopping cart management
   - Methods: `add_item()`, `remove_item()`, `update_quantity()`, `get_total()`, `get_item_count()`, `clear()`

3. **User** (`src/user.py`)
   - User account management
   - Methods: `update_profile()`, `activate_account()`, `deactivate_account()`, `get_cart()`, `clear_cart()`

4. **Order** (`src/order.py`)
   - Order management with status tracking
   - Methods: `confirm_order()`, `process_order()`, `ship_order()`, `deliver_order()`, `cancel_order()`, `get_order_summary()`

5. **Store** (`src/store.py`)
   - Main store management system
   - Methods: `add_product()`, `remove_product()`, `search_products()`, `register_user()`, `create_order()`, `get_store_statistics()`

## Installation

1. Ensure Python 3.7+ is installed
2. No external dependencies required

## Usage

Run the main application to see a demonstration:

```bash
python main.py
```

## Example Usage

```python
from src.store import Store
from src.product import Product
from src.user import User

# Create store
store = Store("My Store")

# Add product
product = Product("P001", "Laptop", 999.99, "High-performance laptop", 10)
store.add_product(product)

# Register user
user = User("U001", "John Doe", "john@example.com")
store.register_user(user)

# Add to cart
user.cart.add_item(product, 1)

# Create order
order = store.create_order("U001")
order.confirm_order()
```

## Class Methods Overview

All classes use instance methods for operations:
- **Product**: Price/stock management, availability checks
- **Cart**: Item management, total calculations
- **User**: Profile management, cart access
- **Order**: Status management, order tracking
- **Store**: Product/user/order management, search functionality

## License

This is a dummy project for educational purposes.

