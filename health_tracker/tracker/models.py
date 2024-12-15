from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()

    def __str__(self):
        return f"{self.activity} on {self.date}"

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.meal_name} on {self.date}"
