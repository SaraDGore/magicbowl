from django.db import models

    
class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    listable = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name


class Cuisine(models.Model):
    CUISINES = (
        ('LATIN', 'Latin'),
        ('SOUTHERN', 'Southern'),
        ('AMERICAN', 'American'),
        ('ASIAN', 'East Asian'),
        ('INDIAN', 'Indian'))
    name = models.CharField(max_length=10, choices=CUISINES)
    
    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    ROLE_CHOICES = (
        ('SAUCE', 'sauce'),
        ('BASE', 'base'),
        ('VEGGIE', 'vegetable'),
        ('PROTEIN', 'protein'),)
        
    name = models.CharField(max_length=200, unique=True)
    ingredients = models.ManyToManyField(Ingredient, through='Recipe_Ingredient')
    cuisines = models.ManyToManyField(Cuisine)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='VEGGIE')
    preparation = models.TextField(max_length=1000)
    source = models.CharField(max_length=300, blank=True)
    
    def __unicode__(self):
        return self.name
    
    
class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=25, blank=True)
    sequence = models.IntegerField(default=1, 
                                    help_text="The order in which the ingredients should appear in the recipe.")
    
    class Meta:
        ordering = ['sequence']
        
    def __unicode__(self):
        i = self.ingredient.name
        return self.amount + ' ' + i
