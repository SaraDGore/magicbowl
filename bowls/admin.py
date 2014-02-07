from django.contrib import admin

from bowls.models import Recipe
from bowls.models import Ingredient
from bowls.models import Recipe_Ingredient

class Recipe_IngredientInline(admin.TabularInline):
    model = Recipe_Ingredient
    extra = 10
    
    
class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 'ingredients',
              'cuisine',
              'role',
              'preparation',
              'source']
    inlines = (Recipe_IngredientInline,)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)

