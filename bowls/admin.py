from django.contrib import admin

from bowls.models import Recipe
from bowls.models import Ingredient
from bowls.models import Recipe_Ingredient
from bowls.models import Cuisine

class Recipe_IngredientInline(admin.TabularInline):
    model = Recipe_Ingredient
    extra = 10

    
class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 
              'role',
              'preparation',
              'source',
              'cuisines',]
    inlines = (Recipe_IngredientInline,)
    filter_horizontal = ('cuisines',)
    list_display = ('name', 'role')
    list_filter = ['role', 'cuisines']
    search_fields = ['name', 'preparation', 'source']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Cuisine)

