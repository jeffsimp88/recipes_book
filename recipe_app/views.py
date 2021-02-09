from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from recipe_app.models import Author, Recipe
from recipe_app.forms import *

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {
        "recipes": recipes
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))

    form = LoginForm()
    return render(request, "generic_form.html", {'form': form, 'heading': "Login as a User"})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})

def author_details(request, author_id):
    author = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, "author_detail.html", {"author": author, "recipes": recipes})

@login_required
def add_recipe(request):
    context = {'heading': "Add a Recipe"}
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            new_item = Recipe.objects.create(
                title=data['title'],
                author = request.user.author,
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions'],

            )
            return HttpResponseRedirect('/')
            

    form = AddRecipeForm()
    context.update({'form': form})
    return render(request, "generic_form.html", context)

@login_required
def add_author(request):
    if request.method == 'POST':
        form=AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect('/')
    form = AddAuthorForm()
    return render(request, "generic_form.html", {'form': form, 'heading': "Add an Author"})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            new_author = Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=new_user
            )
            return HttpResponseRedirect('/')


    form = SignupForm()
    return render(request, "generic_form.html", {'form': form, 'heading': "Signup as a User"})