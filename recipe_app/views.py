from django.shortcuts import render

from recipe_app.models import Author, Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {
        "recipes": recipes
    })

def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})

def author_details(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "author_detail.html", {"author": author})