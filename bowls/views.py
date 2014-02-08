from django.shortcuts import render_to_response

from bowls.models import Cuisine
from bowls.models import Ingredient
from bowls.models import Recipe_Ingredient
from bowls.models import Recipe


def main(request):
    
    ingredients = Ingredient.objects.filter(listable=True)
    cuisines = Cuisine.objects.all()
    
    data = {"ingredients": ingredients,
            "cuisines": cuisines}
            
    
    return render_to_response('base.html', data)
