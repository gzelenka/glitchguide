from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField('name',max_length=64)
    worth = models.FloatField('currants')

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey(Item,related_name='+')
    number = models.IntegerField('amount')

    def __unicode__(self):
        return self.recipe.product.name + "_" + self.ingredient.name
    
class Recipe(models.Model):
    CURRENCY_CHOICES = (
                ('$', 'Currants'),
                ('E','Energy'),
    )
    product = models.ForeignKey(Item,related_name='+')
    #ingredient = models.ForeignKey(Ingredient,related_name='+')
    tool = models.ForeignKey(Item,related_name='+')
    cost = models.IntegerField('cost')
    currency = models.CharField(max_length=1,choices=CURRENCY_CHOICES)

    def __unicode__(self):
        return self.product.name
    
