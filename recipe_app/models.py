from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
"""
User:
---
username
password
email

one to one

Author:
---
name (CharField)
bio (CharField)

one to many

Recipe:
---
title (CharField)
author (ForeignKey)
description (TextField)
Time Required (CharField)
Instructions (TextField)
"""

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
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