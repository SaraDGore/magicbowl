from django.contrib import admin

from bowls.models import Recipe
from bowls.models import Ingredient


admin.site.register(Recipe)
admin.site.register(Ingredient)
