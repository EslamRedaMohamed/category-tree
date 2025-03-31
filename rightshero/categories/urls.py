from django.urls import path
from .views import category_page, get_categories

urlpatterns = [
    path("", category_page, name="category_page"),  # Renders the main category page (HTML template)
    path("categories/", get_categories, name="get_categories"),  # API endpoint to fetch categories (root or by parent ID)
]
