from django.http import JsonResponse
from django.shortcuts import render
from .models import Category

# Fetch categories (Root or by Parent)
def get_categories(request):
    parent_id = request.GET.get("parent")
    categories = Category.objects.filter(parent_id=parent_id) if parent_id else Category.objects.filter(parent__isnull=True)
    return JsonResponse([{"id": cat.id, "name": cat.name} for cat in categories], safe=False)

# Render the category page
def category_page(request):
    return render(request, "index.html")
