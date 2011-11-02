from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from pyglitch.models import Recipe, Item
# Create your views here.

def index(request):
    recipe_list = Recipe.objects.all()
    return render_to_response('glitchguide/index.html',{'recipe_list' : recipe_list})

def recipe(request,recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)
    return render_to_response('glitchguide/recipe.html',{'recipe':r})


