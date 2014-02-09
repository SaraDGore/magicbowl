from django.shortcuts import render_to_response, render

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
        #Maybe make custom methods so these queries aren't so long
        
        if 'cuisine' in request.POST:
            try:
                base = Recipe.objects.filter(role='BASE').filter(cuisines__name__in=request.POST.getlist('cuisine')).order_by('?')[0]
                protein = Recipe.objects.filter(role='PROTEIN').filter(cuisines__name__in=request.POST.getlist('cuisine')).order_by('?')[0]  
                veggie = Recipe.objects.filter(role='VEGGIE').filter(cuisines__name__in=request.POST.getlist('cuisine')).order_by('?')[0] 
                sauce = Recipe.objects.filter(role='SAUCE').filter(cuisines__name__in=request.POST.getlist('cuisine')).order_by('?')[0] 
                bowl = [base, protein, veggie, sauce]
            except:
                data['no_bowl'] = True
                data['bowl'] = True

        else:
            # random selection   
            base = Recipe.objects.filter(role='BASE').order_by('?')[0]
            protein = Recipe.objects.filter(role='PROTEIN').order_by('?')[0]  
            veggie = Recipe.objects.filter(role='VEGGIE').order_by('?')[0] 
            sauce = Recipe.objects.filter(role='SAUCE').order_by('?')[0] 
            bowl = [base, protein, veggie, sauce]
        
        try:
            data['bowl'] = bowl
        except:
            pass
       
    return render(request, 'base.html', data)
