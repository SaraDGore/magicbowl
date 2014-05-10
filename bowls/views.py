from django.shortcuts import render
from django.db.models import Q

from bowls.models import Cuisine
from bowls.models import Ingredient
from bowls.models import Recipe_Ingredient
from bowls.models import Recipe


def main(request):
    
    ingredients = Ingredient.objects.filter(listable=True).order_by('name')
    cuisines = Cuisine.objects.all()
    
    data = {"ingredients": ingredients,
            "cuisines": cuisines}

    if request.POST:
        #TODO: improve error handling
        #Maybe make custom methods so these queries aren't so ridiculous
        data['submitted'] = True
        
        base = Recipe.objects.filter(role='BASE')
        protein = Recipe.objects.filter(role='PROTEIN')
        veggie = Recipe.objects.filter(role='VEGGIE')
        sauce = Recipe.objects.filter(role='SAUCE')

        if 'cuisine' in request.POST and request.POST['cuisine'] != 'ANY':  
            c_list = request.POST.getlist('cuisine')
            base = base.filter(cuisines__name__in=c_list)
            protein = protein.filter(cuisines__name__in=c_list)
            veggie = veggie.filter(cuisines__name__in=c_list)
            sauce = sauce.filter(cuisines__name__in=c_list)
        
        if 'dontuse' in request.POST:
            i_list = request.POST.getlist('dontuse')
            base = base.exclude(ingredients__name__in=i_list)
            protein = protein.exclude(ingredients__name__in=i_list)
            veggie = veggie.exclude(ingredients__name__in=i_list)
            sauce = sauce.exclude(ingredients__name__in=i_list)

        if 'use' in request.POST:
            i_list = request.POST.getlist('use')
            base = base.filter(ingredients__name__in=i_list) or base
            protein = protein.filter(ingredients__name__in=i_list) or protein
            veggie = veggie.filter(ingredients__name__in=i_list) or veggie
            sauce = sauce.filter(ingredients__name__in=i_list) or sauce
        
        base = base.order_by('?')
        protein = protein.order_by('?')
        veggie = veggie.order_by('?')
        sauce = sauce.order_by('?')
        try:
            data['bowl'] = [base[0], protein[0], veggie[0], sauce[0]]
        except:
            pass   
                        
    return render(request, 'bowl.html', data)
