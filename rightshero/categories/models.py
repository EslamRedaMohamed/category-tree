from django.db import models




class Category(models.Model):
    """
    Represents a category in a hierarchical structure.
    
    Attributes:
        name (CharField): The name of the category.
        parent (ForeignKey): A self-referential foreign key that links a category to its parent.
                            - `null=True, blank=True`: Allows root categories (categories without parents).
                            - `related_name="children"`: Allows reverse access to child categories.
                            - `on_delete=models.CASCADE`: Deletes all child categories if the parent is deleted.
    """
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    
    
    """
    Returns a string representation of the category.
    Useful for displaying category names in the Django admin.
    """
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Parent ID: {self.parent.id if self.parent else 'None'}"
