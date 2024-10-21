from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, add_recipe

urlpatterns = [
    path("",views.index, name="index" ),
    path('<int:recipe_id>/', views.single_recipe, name='single_recipe'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('register/', register, name='register'),  # Путь для регистрации
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('accounts/', include('django.contrib.auth.urls')),# Путь для добавления рецепта
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)