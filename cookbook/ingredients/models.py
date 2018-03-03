from django.db import models

# Create your models here.


class Category(models.Model):
    """The category of the ingredient"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """The specific ingredient"""
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(Category, related_name='ingredients',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name
