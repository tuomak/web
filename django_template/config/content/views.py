from django.shortcuts import render, get_object_or_404
from .models import Item
import random

def home_view(request):
    all_items = Item.objects.all()
    latest_items = Item.objects.order_by('-last_done')[:5]
    
    context = {
        'all_items': all_items,
        'latest_items': latest_items,
        
    }
    
    return render(request, 'home.html', context)

def random_item(request):
    random_item = random.choice(Item.objects.all())
    context = {
        'random_item': random_item,
    }
    return render(request, 'item.html', context)