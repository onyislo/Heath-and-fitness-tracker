from django.shortcuts import render, redirect
from .models import Workout, Meal
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def dashboard(request):
    today = date.today()
    workouts = Workout.objects.filter(user=request.user, date=today)
    meals = Meal.objects.filter(user=request.user, date=today)
    total_calories_burned = sum(workout.calories_burned for workout in workouts)
    total_calories_consumed = sum(meal.calories for meal in meals)

    return render(request, 'dashboard.html', {
        'workouts': workouts,
        'meals': meals,
        'total_calories_burned': total_calories_burned,
        'total_calories_consumed': total_calories_consumed,
    })

@login_required
def log_workout(request):
    if request.method == 'POST':
        activity = request.POST['activity']
        duration = int(request.POST['duration'])
        calories_burned = int(request.POST['calories_burned'])
        Workout.objects.create(
            user=request.user,
            date=date.today(),
            activity=activity,
            duration=duration,
            calories_burned=calories_burned
        )
        return redirect('dashboard')
    return render(request, 'log_workout.html')

@login_required
def log_meal(request):
    if request.method == 'POST':
        meal_name = request.POST['meal_name']
        calories = int(request.POST['calories'])
        Meal.objects.create(
            user=request.user,
            date=date.today(),
            meal_name=meal_name,
            calories=calories
        )
        return redirect('dashboard')
    return render(request, 'log_meal.html')
