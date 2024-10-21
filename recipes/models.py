from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Модель категории
class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Модель рецепта
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()  # Можно использовать rich text editor для более сложного форматирования
    cooking_time = models.PositiveIntegerField(help_text="Время приготовления в минутах")
    image = models.ImageField(upload_to='media/recipes', blank=True, null=True)  # Для изображений
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    ingredients = models.TextField(blank=True, null=True)  # Список ингредиентов
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)  # Связь многие ко многим с категориями

    def __str__(self):
        return self.title
