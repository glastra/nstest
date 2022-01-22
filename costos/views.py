from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from .models import Ingredient
from .models import Company
from .models import Restaurant
from .models import Provider
from .models import Receta
from .forms import RecetaForm
from .forms import IngredientForm
from .forms import CompanyForm
from .forms import ProviderForm
from .forms import RestaurantForm
from .forms import StepsForm
from django.http import HttpResponse


def index(request):
    return render(request, 'costos/index.html')

def dashboard(request):
    return render(request, 'costos/dashboard.html')


def company_create(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "costos/company_create.html",
    context)

def company(request):
   return render(request, 'costos/company.html')

class CompanyListView(ListView):
   model = Company

def company_detail(request, pk):
    company = Company.objects.get(pk=pk)

    if request.method == 'POST':
        Provider.save()

        return redirect('provider_list')
    return render(request, 'costos/company_detail.html', {'company': company})

def provider(request):
   return render(request, 'costos/provider.html')

class ProviderListView(ListView):
   model = Provider

def provider_detail(request, pk):
    provider = Provider.objects.get(pk=pk)

    if request.method == 'POST':
        Provider.save()

        return redirect('provider_list')

    return render(request, 'costos/provider_detail.html', {'provider': provider})


def provider_create(request):
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "costos/provider_create.html",
    context)


def restaurant(request):
   return render(request, 'costos/restaurant.html')

class RestaurantListView(ListView):
   model = Restaurant

def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)

    if request.method == 'POST':
        Restaurant.save()

        return redirect('provider_list')

    return render(request, 'costos/restaurant_detail.html', {'restaurant': restaurant})


def restaurant_create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "costos/restaurant_create.html",
    context)


def ingredient_create(request):
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "costos/ingredient_create.html",
    context)

class IngredientListView(ListView):
   model = Ingredient


def ingredient_detail(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)

    if request.method == 'POST':
        Ingredient.save()

        return redirect('ingredient_list')

    return render(request, 'costos/ingredient_detail.html', {'ingredient': ingredient})

class RecetaListView(ListView):
   model = Receta

def receta(request):
   return render(request, 'costos/receta.html')


def receta_create(request):
    form = RecetaForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "costos/receta_create.html",
    context)


def receta_detail(request, pk):
    receta = Receta.objects.get(pk=pk)

    if request.method == 'POST':
        Receta.save()

        return redirect('recetalist')

    return render(request, 'costos/restaurant_detail.html', {'restaurant': restaurant})


def login(request):
   return render(request, 'costos/login.html')


def register(request):
   return render(request, 'costos/register.html')


def forgot_password(request):
   return render(request, 'costos/forgot-password.html')


def buttons(request):
   return render(request, 'costos/buttons.html')
