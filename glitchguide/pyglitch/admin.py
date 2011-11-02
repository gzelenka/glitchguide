from pyglitch.models import Item, Ingredient, Recipe
from django.contrib import admin

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 6

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product',  {'fields': ['product']}),
        ('Tool', {'fields': ['tool']}),
        ('Cost', {'fields': ['cost','currency']}),
    ]
    inlines = [IngredientInline]
        


admin.site.register(Item)
admin.site.register(Ingredient)
admin.site.register(Recipe,RecipeAdmin)
