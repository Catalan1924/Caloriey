from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import FoodItem
from django.db.models import Sum

def food_list(request):
    today = timezone.now().date()
    items = FoodItem.objects.filter(date=today)
    total = items.aggregate(total_cals=Sum('calories'))['total_cals'] or 0
    return render(request, 'food_list.html', {'items': items, 'total': total})

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name'].strip()
        cals = int(request.POST['calories'])
        FoodItem.objects.create(name=name, calories=cals)
    return redirect('food_list')

def delete_food(request, pk):
    get_object_or_404(FoodItem, pk=pk).delete()
    return redirect('food_list')

def reset_day(request):
    FoodItem.objects.filter(date=timezone.now().date()).delete()
    return redirect('food_list')