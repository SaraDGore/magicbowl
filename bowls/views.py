from django.shortcuts import render_to_response

from bowls.models import Cuisine
from bowls.models import Ingredient
from bowls.models import Recipe_Ingredient
from bowls.models import Recipe


def main(request):
    
    ingredients = Ingredient.objects.filter(listable=True)
    cuisines = Cuisine.objects.all()
    
    # random selection   
    base = Recipe.objects.filter(role='BASE').order_by('?')[:1]
    protein = Recipe.objects.filter(role='PROTEIN').order_by('?')[:1]  
    veggie = Recipe.objects.filter(role='VEGGIE').order_by('?')[:1] 
    sauce = Recipe.objects.filter(role='SAUCE').order_by('?')[:1] 
    bowl = [base[0], protein[0], veggie[0], sauce[0]]

    data = {"ingredients": ingredients,
            "cuisines": cuisines,
            "bowl": bowl}
            
    return render_to_response('base.html', data)
