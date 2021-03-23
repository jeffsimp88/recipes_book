# Generated by Django 3.1.6 on 2021-03-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorite_recipes',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite_recipes', to='recipe_app.Recipe'),
        ),
    ]
