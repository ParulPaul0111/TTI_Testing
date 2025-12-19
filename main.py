"""
Main application file to demonstrate the e-commerce system
"""

from src.store import Store
from src.product import Product
from src.user import User


def main():
    """Main function to demonstrate the e-commerce system"""
    
    # Create a store
    store = Store("My E-Commerce Store")
    
    # Add products to the store
    print("=" * 50)
    print("Adding Products to Store")
    print("=" * 50)
    
    products_data = [
        ("P001", "Laptop", 999.99, "High-performance laptop", 10),
        ("P002", "Mouse", 29.99, "Wireless mouse", 50),
        ("P003", "Keyboard", 79.99, "Mechanical keyboard", 25),
        ("P004", "Monitor", 299.99, "27-inch 4K monitor", 15),
        ("P005", "Headphones", 149.99, "Noise-cancelling headphones", 30),
    ]
    
    for prod_id, name, price, desc, stock in products_data:
        product = Product(prod_id, name, price, desc, stock)
        store.add_product(product)
        print(f"Added: {product}")
    
    print()
    
    # Register users
    print("=" * 50)
    print("Registering Users")
    print("=" * 50)
    
    user1 = User("U001", "John Doe", "john@example.com", "123 Main St, City")
    user2 = User("U002", "Jane Smith", "jane@example.com", "456 Oak Ave, City")
    
    store.register_user(user1)
    store.register_user(user2)
    
    print(f"Registered: {user1}")
    print(f"Registered: {user2}")
    print()
    
    # User 1 adds items to cart
    print("=" * 50)
    print("User 1 Shopping Cart")
    print("=" * 50)
    
    laptop = store.get_product("P001")
    mouse = store.get_product("P002")
    keyboard = store.get_product("P003")
    
    user1.cart.add_item(laptop, 1)
    user1.cart.add_item(mouse, 2)
    user1.cart.add_item(keyboard, 1)
    
    print(f"Cart: {user1.cart}")
    print("\nCart Items:")
    for prod_id, details in user1.cart.get_cart_items().items():
        print(f"  - {details['name']}: {details['quantity']}x ${details['price']:.2f} = ${details['subtotal']:.2f}")
    print(f"Total: ${user1.cart.get_total():.2f}")
    print()
    
    # User 1 places an order
    print("=" * 50)
    print("User 1 Places Order")
    print("=" * 50)
    
    order1 = store.create_order("U001", "123 Main St, City")
    if order1:
        print(f"Order Created: {order1}")
        order1.confirm_order()
        print(f"Order Status: {order1.status.value}")
        print()
    
    # User 2 adds items to cart
    print("=" * 50)
    print("User 2 Shopping Cart")
    print("=" * 50)
    
    monitor = store.get_product("P004")
    headphones = store.get_product("P005")
    
    user2.cart.add_item(monitor, 1)
    user2.cart.add_item(headphones, 1)
    
    print(f"Cart: {user2.cart}")
    print("\nCart Items:")
    for prod_id, details in user2.cart.get_cart_items().items():
        print(f"  - {details['name']}: {details['quantity']}x ${details['price']:.2f} = ${details['subtotal']:.2f}")
    print(f"Total: ${user2.cart.get_total():.2f}")
    print()
    
    # User 2 places an order
    print("=" * 50)
    print("User 2 Places Order")
    print("=" * 50)
    
    order2 = store.create_order("U002")
    if order2:
        print(f"Order Created: {order2}")
        order2.confirm_order()
        order2.process_order()
        order2.ship_order()
        order2.deliver_order()
        print(f"Order Status: {order2.status.value}")
        print()
    
    # Search products
    print("=" * 50)
    print("Search Products")
    print("=" * 50)
    
    search_results = store.search_products("laptop")
    print(f"Search results for 'laptop': {len(search_results)} found")
    for product in search_results:
        print(f"  - {product}")
    print()
    
    # Store statistics
    print("=" * 50)
    print("Store Statistics")
    print("=" * 50)
    
    stats = store.get_store_statistics()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key.replace('_', ' ').title()}: ${value:.2f}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")
    print()
    
    # Display order details
    print("=" * 50)
    print("Order Details")
    print("=" * 50)
    
    for order_id in store.orders.keys():
        order = store.get_order(order_id)
        print(f"\n{order}")
        summary = order.get_order_summary()
        print(f"  Items: {len(summary['items'])}")
        print(f"  Status: {summary['status']}")
        print(f"  Order Date: {summary['order_date']}")


if __name__ == "__main__":
    main()

