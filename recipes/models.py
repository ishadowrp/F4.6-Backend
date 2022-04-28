from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='RecipeCategory')
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()
    cooking_method = models.TextField()
    photo1 = models.ImageField(upload_to='photos', max_length=254, blank=True, null=True)
    photo2 = models.ImageField(upload_to='photos', max_length=254, blank=True, null=True)
    photo3 = models.ImageField(upload_to='photos', max_length=254, blank=True, null=True)
    rating = models.IntegerField(default=0)

    @property
    def in_category(self):
        list_of_category = [category.name for category in self.category.all()]
        return list_of_category

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:125] + '...'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с новостью
        return f'/posts/{self.id}'

    def __str__(self):
        return f'{self.title}'


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
