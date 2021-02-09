from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_app.models import Author, Recipe
from recipe_app.forms import AddRecipeForm, AddAuthorForm

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
    recipes = Recipe.objects.filter(author=author)
    return render(request, "author_detail.html", {"author": author, "recipes": recipes})

def add_recipe(request):
    context = {'heading': "Add a Recipe"}
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            new_item = Recipe.objects.create(
                title=data['title'],
                author = data['author'],
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions'],

            )
            return HttpResponseRedirect('/')
            

    form = AddRecipeForm()
    context.update({'form': form})
    return render(request, "generic_form.html", context)

def add_author(request):
    if request.method == 'POST':
        form=AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect('/')
    form = AddAuthorForm()
    return render(request, "generic_form.html", {'form': form, 'heading': "Add an Author"})