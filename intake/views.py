from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import WaterIntake
from .forms import WaterIntakeForm, DateRangeForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum
from django.utils import timezone

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

@login_required
def add_intake(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            intake = form.save(commit=False)
            intake.user = request.user
            current_date = timezone.localtime().date()

            if not WaterIntake.objects.filter(user=request.user, date=current_date).exists():
                intake.save()
                messages.success(request, 'Intake added successfully.')
                return redirect('add_intake')            
            else:
                messages.error(request, 'You can only add one entry per day.')
                form = WaterIntakeForm()
    else:
        form = WaterIntakeForm()
    return render(request, 'add_intake.html', {'form': form})

@login_required
def view_intakes(request):
    intakes = WaterIntake.objects.filter(user=request.user)
    return render(request, 'view_intakes.html', {'intakes': intakes})

def edit_intake(request, pk):
    intake = WaterIntake.objects.get(pk=pk)
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST, instance=intake)
        if form.is_valid():
            form.save()
            messages.success(request, 'Intake updated successfully.')
            return redirect('view_intakes')
    else:
        form = WaterIntakeForm(instance=intake)
    return render(request, 'add_intake.html', {'form': form})

def delete_intake(request, pk):
    intake = WaterIntake.objects.get(pk=pk)
    if request.method == "POST" and 'confirm_delete' in request.POST:
        # intake = WaterIntake.objects.get(pk=pk)
        intake.delete()
        messages.success(request, 'Intake deleted successfully.')
        return redirect('view_intakes')
    else:
        return render(request, 'delete.html', {'user': request.user, 'intake': intake})

@login_required
def list_intakes(request):
    intakes = WaterIntake.objects.filter(user=request.user)
    paginator = Paginator(intakes, 2)  
    page = request.GET.get('page')
    intakes = paginator.get_page(page)
    return render(request, 'all_intakes.html', {'intakes': intakes})

@login_required
def find_difference(request):
    difference = None
    
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']
            intake1 = WaterIntake.objects.filter(user=request.user, date=date1).aggregate(Sum('quantity'))['quantity__sum'] or 0
            intake2 = WaterIntake.objects.filter(user=request.user, date=date2).aggregate(Sum('quantity'))['quantity__sum'] or 0
            if intake1 or intake2 == 0:
                messages.error(request, 'Incorrect date chosen')
            else:
                difference = intake2 - intake1
    else:
        form = DateRangeForm()
    return render(request, 'find_difference.html', {'form': form, 'difference': difference})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)