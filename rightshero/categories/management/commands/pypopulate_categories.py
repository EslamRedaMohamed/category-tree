from django.core.management.base import BaseCommand
from categories.models import Category
from django.db import connection

class Command(BaseCommand):
    help = "Clear and populate the database with categories up to 3 levels."

    def handle(self, *args, **kwargs):
        # 🔹 Clear existing data
        Category.objects.all().delete()

        # 🔹 Reset ID sequence (PostgreSQL only)
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE categories_category_id_seq RESTART WITH 1;")

        # 🔹 Level 0 (Root)
        cat_a = Category.objects.create(name="Category A")
        cat_b = Category.objects.create(name="Category B")

        # 🔹 Level 1
        sub_a1 = Category.objects.create(name="A-1", parent=cat_a)
        sub_a2 = Category.objects.create(name="A-2", parent=cat_a)  
        sub_b1 = Category.objects.create(name="B-1", parent=cat_b)
        sub_b2 = Category.objects.create(name="B-2", parent=cat_b)  

        # 🔹 Level 2
        sub_a11 = Category.objects.create(name="A1-1", parent=sub_a1)
        sub_a12 = Category.objects.create(name="A1-2", parent=sub_a1)
        sub_a21 = Category.objects.create(name="A2-1", parent=sub_a2)  
        sub_a22 = Category.objects.create(name="A2-2", parent=sub_a2)  

        sub_b11 = Category.objects.create(name="B1-1", parent=sub_b1)
        sub_b12 = Category.objects.create(name="B1-2", parent=sub_b1)
        sub_b21 = Category.objects.create(name="B2-1", parent=sub_b2)  
        sub_b22 = Category.objects.create(name="B2-2", parent=sub_b2)  

        # 🔹 Level 3
        Category.objects.create(name="A11-1", parent=sub_a11)
        Category.objects.create(name="A11-2", parent=sub_a11)
        Category.objects.create(name="A12-1", parent=sub_a12)
        Category.objects.create(name="A12-2", parent=sub_a12)

        Category.objects.create(name="B11-1", parent=sub_b11)
        Category.objects.create(name="B11-2", parent=sub_b11)
        Category.objects.create(name="B12-1", parent=sub_b12)
        Category.objects.create(name="B12-2", parent=sub_b12)

        Category.objects.create(name="A21-1", parent=sub_a21)  
        Category.objects.create(name="A21-2", parent=sub_a21) 
        Category.objects.create(name="A22-1", parent=sub_a22)  
        Category.objects.create(name="A22-2", parent=sub_a22)  

        Category.objects.create(name="B21-1", parent=sub_b21)  
        Category.objects.create(name="B21-2", parent=sub_b21)  
        Category.objects.create(name="B22-1", parent=sub_b22)  
        Category.objects.create(name="B22-2", parent=sub_b22)  

        self.stdout.write(self.style.SUCCESS("Categories cleared and populated successfully."))
