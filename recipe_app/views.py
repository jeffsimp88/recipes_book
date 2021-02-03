from django.shortcuts import render

from recipe_app.models import Author, Recipe

# Create your views here.
def index(request):
    return render(request, "index.html")