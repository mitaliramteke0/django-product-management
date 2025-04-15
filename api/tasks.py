import json
from celery import shared_task
from .models import Category, Product

@shared_task
def bulk_upload(data):
    data = json.loads(data)
    for cat in data.get('categories', []):
        Category.objects.create(**cat)
    for prod in data.get('products', []):
        Product.objects.create(**prod)