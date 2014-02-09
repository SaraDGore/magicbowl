from django.shortcuts import render_to_response, render

from bowls.models import Cuisine
from bowls.models import Ingredient
from bowls.models import Recipe_Ingredient
from bowls.models import Recipe


def main(request):
    
    ingredients = Ingredient.objects.filter(listable=True).order_by('name')
    cuisines = Cuisine.objects.all()
    
    no_bowl = False
    
    data = {"ingredients": ingredients,
            "cuisines": cuisines}

    if request.POST:
        #TODO: improve error handling
        #Maybe make custom methods so these queries aren't so long
        
        if 'surprise' in request.POST:
            #TODO: want a way to drop to bottom if this is picked besides a huge ELSE loop
            base = Recipe.objects.filter(role='BASE').order_by('?')[0]
            protein = Recipe.objects.filter(role='PROTEIN').order_by('?')[0]  
            veggie = Recipe.objects.filter(role='VEGGIE').order_by('?')[0]
            sauce = Recipe.objects.filter(role='SAUCE').order_by('?')[0] 
            data['bowl'] = [base, protein, veggie, sauce]
        else:
            if 'cuisine' in request.POST and request.POST['cuisine'] != 'ANY':
                try:
                    c_list = request.POST.getlist('cuisine')
                    base = Recipe.objects.filter(role='BASE').filter(cuisines__name__in=c_list).order_by('?')
                    protein = Recipe.objects.filter(role='PROTEIN').filter(cuisines__name__in=c_list).order_by('?')  
                    veggie = Recipe.objects.filter(role='VEGGIE').filter(cuisines__name__in=c_list).order_by('?') 
                    sauce = Recipe.objects.filter(role='SAUCE').filter(cuisines__name__in=c_list).order_by('?') 
                except:
                    no_bowl = True

            if not no_bowl:
                if 'dontuse' in request.POST:
                    try:
                        i_list = request.POST.getlist('dontuse')
                        base = base.exclude(ingredients__name__in=i_list).order_by('?')
                        protein = protein.exclude(ingredients__name__in=i_list).order_by('?')
                        veggie = veggie.exclude(ingredients__name__in=i_list).order_by('?')
                        sauce = sauce.exclude(ingredients__name__in=i_list).order_by('?')
                    except:
                        no_bowl = True
            
            # need to add an inclusion stuff too, but the math for that will be different
    
        if no_bowl:
            # TODO: make another method of keying the js off
            data['no_bowl'] = True
            data['bowl'] = True # this is here because right now the js is keying off of bowl existing
        else:
            try:
                data['bowl'] = [base[0], protein[0], veggie[0], sauce[0]]
            except: 
                print 'what just happened?'
                pass # TODO: add erorr handlign
       
    return render(request, 'base.html', data)
