"""
Product class for managing e-commerce products
"""


class Product:
    """Represents a product in the e-commerce system"""
    
    def __init__(self, product_id: str, name: str, price: float, description: str = "", stock: int = 0):
        """
        Initialize a product
        
        Args:
            product_id: Unique identifier for the product
            name: Product name
            price: Product price
            description: Product description
            stock: Available stock quantity
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock
    
    def update_price(self, new_price: float) -> bool:
        """
        Update the product price
        
        Args:
            new_price: New price for the product
            
        Returns:
            bool: True if price updated successfully
        """
        if new_price < 0:
            return False
        self.price = new_price
        return True
    
    def update_stock(self, quantity: int) -> bool:
        """
        Update the product stock
        
        Args:
            quantity: Quantity to add (positive) or remove (negative)
            
        Returns:
            bool: True if stock updated successfully
        """
        new_stock = self.stock + quantity
        if new_stock < 0:
            return False
        self.stock = new_stock
        return True
    
    def is_available(self) -> bool:
        """
        Check if product is available in stock
        
        Returns:
            bool: True if stock > 0
        """
        return self.stock > 0
    
    def get_discount_price(self, discount_percent: float) -> float:
        """
        Calculate discounted price
        
        Args:
            discount_percent: Discount percentage (0-100)
            
        Returns:
            float: Discounted price
        """
        if discount_percent < 0 or discount_percent > 100:
            return self.price
        discount_amount = self.price * (discount_percent / 100)
        return self.price - discount_amount
    
    def __str__(self) -> str:
        """String representation of the product"""
        return f"Product(id={self.product_id}, name={self.name}, price=${self.price:.2f}, stock={self.stock})"
    
    def __repr__(self) -> str:
        """Official string representation"""
        return f"Product('{self.product_id}', '{self.name}', {self.price}, '{self.description}', {self.stock})"

