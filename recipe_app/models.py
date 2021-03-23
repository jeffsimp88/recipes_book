from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_recipes = models.ManyToManyField("Recipe", related_name='favorite_recipes', blank=True)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=150)
    instructions = models.TextField()
    def __str__(self):
        return f"{self.title} | {self.author}"