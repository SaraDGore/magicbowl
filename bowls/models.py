from django.db import models

ROLE_CHOICES = (
    ('SAUCE', 'sauce'),
    ('BASE', 'base'),
    ('VEGGIE', 'vegetable'),
    ('PROTEIN', 'protein'),)
    
CUISINES = (
    ('LATIN', 'Latin'),
    ('SOUTHERN', 'Southern'),
    ('AMERICAN', 'American'),
    ('ASIAN', 'East Asian'),
    ('INDIAN', 'Indian'))
    
class Ingredient(models.Model):
    name = models.CharField(max_length=200)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = ManyToManyField(Ingredient, through='Recipe_Ingredient')
    cuisine = models.CharField(max_length=10, choices=CUISINES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    preparation = models.TextField(max_length=1000)
    source = models.CharField(max_length=300)
    
class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=10)
