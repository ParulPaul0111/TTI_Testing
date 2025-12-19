"""
Order class for managing e-commerce orders
"""

from datetime import datetime
from typing import Dict, List
from enum import Enum
from src.cart import Cart


class OrderStatus(Enum):
    """Order status enumeration"""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order:
    """Represents an order in the e-commerce system"""
    
    def __init__(self, order_id: str, user_id: str, cart: Cart, shipping_address: str = ""):
        """
        Initialize an order
        
        Args:
            order_id: Unique identifier for the order
            user_id: ID of the user placing the order
            cart: Cart object containing items
            shipping_address: Shipping address for the order
        """
        self.order_id = order_id
        self.user_id = user_id
        self.items = cart.get_cart_items().copy()
        self.shipping_address = shipping_address
        self.total_amount = cart.get_total()
        self.status = OrderStatus.PENDING
        self.order_date = datetime.now()
        self.delivery_date = None
    
    def confirm_order(self) -> bool:
        """
        Confirm the order
        
        Returns:
            bool: True if order confirmed successfully
        """
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.CONFIRMED
            return True
        return False
    
    def process_order(self) -> bool:
        """
        Mark order as processing-test
        
        Returns:
            bool: True if order status updated successfully
        """
        if self.status == OrderStatus.CONFIRMED:
            self.status = OrderStatus.PROCESSING
            return True
        return False
    
    def ship_order(self) -> bool:
        """
        Mark order as shipped
        
        Returns:
            bool: True if order status updated successfully
        """
        if self.status == OrderStatus.PROCESSING:
            self.status = OrderStatus.SHIPPED
            return True
        return False
    
    def deliver_order(self) -> bool:
        """
        Mark order as delivered
        
        Returns:
            bool: True if order status updated successfully
        """
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.delivery_date = datetime.now()
            return True
        return False
    
    def cancel_order(self) -> bool:
        """
        Cancel the order
        
        Returns:
            bool: True if order cancelled successfully
        """
        if self.status not in [OrderStatus.DELIVERED, OrderStatus.CANCELLED]:
            self.status = OrderStatus.CANCELLED
            return True
        return False
    
    def update_shipping_address(self, new_address: str) -> bool:
        """
        Update shipping address
        
        Args:
            new_address: New shipping address
            
        Returns:
            bool: True if address updated successfully
        """
        if self.status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
            return False
        self.shipping_address = new_address
        return True
    
    def get_order_summary(self) -> Dict:
        """
        Get order summary
        
        Returns:
            Dict: Order summary with all details
        """
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'items': self.items,
            'total_amount': self.total_amount,
            'status': self.status.value,
            'order_date': self.order_date.strftime("%Y-%m-%d %H:%M:%S"),
            'shipping_address': self.shipping_address,
            'delivery_date': self.delivery_date.strftime("%Y-%m-%d %H:%M:%S") if self.delivery_date else None
        }
    
    def __str__(self) -> str:
        """String representation of the order"""
        return f"Order(id={self.order_id}, user={self.user_id}, total=${self.total_amount:.2f}, status={self.status.value})"
    
    def __repr__(self) -> str:
        """Official string representation"""
        return f"Order('{self.order_id}', '{self.user_id}', {self.total_amount}, '{self.status.value}')"

