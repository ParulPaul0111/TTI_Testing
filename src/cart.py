"""
Shopping Cart class for managing user's cart items
"""

from typing import Dict
from src.product import Product


class Cart:
    """Represents a shopping cart for a user"""
    
    def __init__(self, user_id: str):
        """
        Initialize a shopping cart
        
        Args:
            user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.items: Dict[str, int] = {}  # {product_id: quantity}
        self.products: Dict[str, Product] = {}  # {product_id: Product}
    
    def add_item(self, product: Product, quantity: int = 1) -> bool:
        """
        Add a product to the cart
        
        Args:
            product: Product object to add
            quantity: Quantity to add
            
        Returns:
            bool: True if item added successfully
        """
        if quantity <= 0:
            return False
        
        if not product.is_available():
            return False
        
        if product.stock < quantity:
            return False
        
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity
            self.products[product.product_id] = product
        
        return True
    
    def remove_item(self, product_id: str, quantity: int = None) -> bool:
        """
        Remove a product from the cart
        
        Args:
            product_id: ID of the product to remove
            quantity: Quantity to remove (None removes all)
            
        Returns:
            bool: True if item removed successfully
        """
        if product_id not in self.items:
            return False
        
        if quantity is None:
            del self.items[product_id]
            del self.products[product_id]
        else:
            self.items[product_id] -= quantity
            if self.items[product_id] <= 0:
                del self.items[product_id]
                del self.products[product_id]
        
        return True
    
    def update_quantity(self, product_id: str, quantity: int) -> bool:
        """
        Update the quantity of a product in the cart
        
        Args:
            product_id: ID of the product
            quantity: New quantity
            
        Returns:
            bool: True if quantity updated successfully
        """
        if product_id not in self.items:
            return False
        
        if quantity <= 0:
            return self.remove_item(product_id)
        
        product = self.products[product_id]
        if product.stock < quantity:
            return False
        
        self.items[product_id] = quantity
        return True
    
    def get_total(self) -> float:
        """
        Calculate the total price of all items in the cart
        
        Returns:
            float: Total price
        """
        total = 0.0
        for product_id, quantity in self.items.items():
            product = self.products[product_id]
            total += product.price * quantity
        return total
    
    def get_item_count(self) -> int:
        """
        Get the total number of items in the cart
        
        Returns:
            int: Total item count
        """
        return sum(self.items.values())
    
    def clear(self) -> None:
        """Clear all items from the cart"""
        self.items.clear()
        self.products.clear()
    
    def get_cart_items(self) -> Dict[str, Dict]:
        """
        Get all cart items with details
        
        Returns:
            Dict: Cart items with product details and quantities
        """
        cart_details = {}
        for product_id, quantity in self.items.items():
            product = self.products[product_id]
            cart_details[product_id] = {
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'subtotal': product.price * quantity
            }
        return cart_details
    
    def __str__(self) -> str:
        """String representation of the cart"""
        return f"Cart(user_id={self.user_id}, items={self.get_item_count()}, total=${self.get_total():.2f})"

