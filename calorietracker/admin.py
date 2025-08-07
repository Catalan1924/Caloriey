from django.contrib import admin
from .models import FoodItem, MealEntry, DailyGoal

admin.site.register(FoodItem)
admin.site.register(MealEntry)
admin.site.register(DailyGoal)