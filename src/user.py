"""
User class for managing e-commerce users.
"""

from typing import Optional
from src.cart import Cart


class User:
    """Represents a user in the e-commerce system"""
    
    def __init__(self, user_id: str, name: str, email: str, address: str = ""):
        """
        Initialize a user
        
        Args:
            user_id: Unique identifier for the user
            name: User's full name
            email: User's email address
            address: User's address
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.cart = Cart(user_id)
        self.is_active = True
    
    def update_profile(self, name: Optional[str] = None, email: Optional[str] = None, 
                      address: Optional[str] = None) -> bool:
        """
        Update user profile informations
        
        Args:
            name: New name (optional)
            email: New email (optional)
            address: New address (optional)
            
        Returns:
            bool: True if profile updated successfully
        """
        if name:
            self.name = name
        if email:
            self.email = email
        if address:
            self.address = address
        return True
    
    def activate_account(self) -> None:
        """Activate the user account"""
        self.is_active = True
    
    def deactivate_account(self) -> None:
        """Deactivate the user account"""
        self.is_active = False
    
    def get_cart(self) -> Cart:
        """
        Get the user's shopping cart
        
        Returns:
            Cart: User's cart object
        """
        return self.cart
    
    def clear_cart(self) -> None:
        """Clear the user's shopping cart"""
        self.cart.clear()
    
    def __str__(self) -> str:
        """String representation of the user"""
        status = "Active" if self.is_active else "Inactive"
        return f"User(id={self.user_id}, name={self.name}, email={self.email}, status={status})"
    
    def __repr__(self) -> str:
        """Official string representation"""
        return f"User('{self.user_id}', '{self.name}', '{self.email}', '{self.address}')"

    def __repr__(self) -> str:
        """Official string representations"""
        return f"User('{self.user_id}', '{self.name}', '{self.email}', '{self.address}')"