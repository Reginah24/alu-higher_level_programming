# models/square.py
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """String representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
