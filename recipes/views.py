from django.shortcuts import render, redirect
from .models import Recipe
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, RecipeForm




@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Присваиваем автору рецепт текущего пользователя
            recipe.save()
            return redirect('index')  # Перенаправляем на главную страницу
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})




def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def single_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'single_recipe.html', {'recipe': recipe})

def search_recipes(request):
    query = request.GET.get('query', '')
    recipes = Recipe.objects.filter(title__icontains=query) if query else []
    return render(request, 'index.html', {'recipes': recipes})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Путь на главную страницу или куда нужно
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})