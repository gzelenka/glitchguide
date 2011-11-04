from django.db import models

# Create your models here.


class Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey('Item',related_name='+')
    number = models.IntegerField('amount')

    def __unicode__(self):
        return self.recipe.product.name + "_" + self.ingredient.name
    
class Recipe(models.Model):
    CURRENCY_CHOICES = (
                ('$', 'Currants'),
                ('E','Energy'),
    )
    product = models.ForeignKey('Item',related_name='+')
    tool = models.ForeignKey('Item',related_name='+')
    cost = models.IntegerField('cost')
    currency = models.CharField(max_length=1,choices=CURRENCY_CHOICES)

    def __unicode__(self):
        return self.product.name
   
    def getTotalCost(self):
        total = { 'E' : 0,
                  '$' : 0,
               }
        total[str(self.currency)] = self.cost
        for i in self.ingredient_set.all():
            try:
                r = Recipe.objects.get(product=i.ingredient)
                c = r.getTotalCost()
                total['E'] += (c['E'] * i.number)
                total['$'] += (c['$'] * i.number)
            except:
                pass
        return total
    def printTotalCost(self):
        amount = self.getTotalCost()
        return "Total cost is " + str(amount['E']) + " energy and " + str(amount['$']) + " currants."

class Item(models.Model):
    name = models.CharField('name',max_length=64)
    worth = models.FloatField('currants')
    def __unicode__(self):
        return self.name
    def getRecipe(self):
        try:
            i = Recipe.objects.get(product=self).id
        except:
            return ""
        return i
