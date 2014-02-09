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
        data['submitted'] = True
        no_bowl = False
        
        if 'surprise' in request.POST:
            #I could tie this into the logic below but this saves a bit of processing I think
            base = Recipe.objects.filter(role='BASE').order_by('?')[0]
            protein = Recipe.objects.filter(role='PROTEIN').order_by('?')[0]  
            veggie = Recipe.objects.filter(role='VEGGIE').order_by('?')[0]
            sauce = Recipe.objects.filter(role='SAUCE').order_by('?')[0] 
            data['bowl'] = [base, protein, veggie, sauce]
            return render(request, 'base.html', data)

        if 'cuisine' in request.POST:
            try: 
                if request.POST['cuisine'] == 'ANY':
                    base = Recipe.objects.filter(role='BASE').order_by('?')
                    protein = Recipe.objects.filter(role='PROTEIN').order_by('?')  
                    veggie = Recipe.objects.filter(role='VEGGIE').order_by('?')
                    sauce = Recipe.objects.filter(role='SAUCE').order_by('?') 
                else: 
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
        
        try:
            data['bowl'] = [base[0], protein[0], veggie[0], sauce[0]]
        except: 
            pass
            
    return render(request, 'base.html', data)
