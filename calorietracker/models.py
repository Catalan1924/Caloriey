from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class FoodItem(models.Model):
    name = models.CharField(max_length=120)
    calories = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"

class MealEntry(models.Model):
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    time = models.TimeField(default=timezone.now)

class DailyGoal(models.Model):
    target_calories = models.PositiveIntegerField(default=2000)
    date = models.DateField(default=timezone.now)