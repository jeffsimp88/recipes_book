# Generated by Django 3.1.6 on 2021-03-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_author_favorite_recipes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='favorite_recipes',
            field=models.ManyToManyField(blank=True, related_name='favorite_recipes', to='recipe_app.Recipe'),
        ),
    ]
