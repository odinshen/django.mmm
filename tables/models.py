from django.db import models

# Create your models here.
class Table(models.Model):
    meal = models.CharField(max_length=100)
    chef = models.TextField(blank=True)
    recipes = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meal
    