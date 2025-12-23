"""
Store class for managing the e-commerce store.
"""

from typing import Dict, List, Optional
from src.product import Product
from src.user import User
from src.order import Order, OrderStatus


class Store:
    """Represents the main e-commerce store"""
    
    def __init__(self, store_name: str):
        """
        Initialize the store
        
        Args:
            store_name: Name of the store
        """
        self.store_name = store_name
        self.products: Dict[str, Product] = {}
        self.users: Dict[str, User] = {}
        self.orders: Dict[str, Order] = {}
    
    def add_product(self, product: Product) -> bool:
        """
        Add a product to the store
        
        Args:
            product: Product object to add
            
        Returns:
            bool: True if product added successfully
        """
        if product.product_id in self.products:
            return False
        self.products[product.product_id] = product
        return True
    
    def remove_product(self, product_id: str) -> bool:
        """
        Remove a product from the store
        
        Args:
            product_id: ID of the product to remove
            
        Returns:
            bool: True if product removed successfully
        """
        if product_id not in self.products:
            return False
        del self.products[product_id]
        return True
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """
        Get a product by ID
        
        Args:
            product_id: ID of the product
            
        Returns:
            Product or None if not found
        """
        return self.products.get(product_id)
    
    def search_products(self, keyword: str) -> List[Product]:
        """
        Search products by keyword
        
        Args:
            keyword: Search keyword
            
        Returns:
            List of matching products
        """
        keyword_lower = keyword.lower()
        results = []
        for product in self.products.values():
            if (keyword_lower in product.name.lower() or 
                keyword_lower in product.description.lower()):
                results.append(product)
        return results
    
    def get_available_products(self) -> List[Product]:
        """
        Get all available products (in stock)
        
        Returns:
            List of available products
        """
        return [product for product in self.products.values() if product.is_available()]
    
    def register_user(self, user: User) -> bool:
        """
        Register a new user
        
        Args:
            user: User object to register
            
        Returns:
            bool: True if user registered successfully
        """
        if user.user_id in self.users:
            return False
        self.users[user.user_id] = user
        return True
    
    def get_user(self, user_id: str) -> Optional[User]:
        """
        Get a user by ID
        
        Args:
            user_id: ID of the user
            
        Returns:
            User or None if not found
        """
        return self.users.get(user_id)
    
    def create_order(self, user_id: str, shipping_address: str = "") -> Optional[Order]:
        """
        Create an order from user's cart
        
        Args:
            user_id: ID of the user
            shipping_address: Shipping address
            
        Returns:
            Order object or None if creation failed
        """
        user = self.get_user(user_id)
        if not user:
            return None
        
        if user.cart.get_item_count() == 0:
            return None
        
        order_id = f"ORD-{len(self.orders) + 1:06d}"
        order = Order(order_id, user_id, user.cart, shipping_address or user.address)
        self.orders[order_id] = order
        
        # Clear user's cart after order creation
        user.clear_cart()
        
        return order
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """
        Get an order by ID
        
        Args:
            order_id: ID of the order
            
        Returns:
            Order or None if not found
        """
        return self.orders.get(order_id)
    
    def get_user_orders(self, user_id: str) -> List[Order]:
        """
        Get all orders for a user
        
        Args:
            user_id: ID of the user
            
        Returns:
            List of orders
        """
        return [order for order in self.orders.values() if order.user_id == user_id]
    
    def get_store_statistics(self) -> Dict:
        """
        Get store statistics
        
        Returns:
            Dict: Store statistics
        """
        total_revenue = sum(
            order.total_amount 
            for order in self.orders.values() 
            if order.status == OrderStatus.DELIVERED
        )
        
        return {
            'store_name': self.store_name,
            'total_products': len(self.products),
            'available_products': len(self.get_available_products()),
            'total_users': len(self.users),
            'total_orders': len(self.orders),
            'total_revenue': total_revenue
        }
    
    def __str__(self) -> str:
        """String representation of the store"""
        return f"Store(name={self.store_name}, products={len(self.products)}, users={len(self.users)}, orders={len(self.orders)})"

