from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, unique=True, db_index=True)
    slug = models.SlugField(max_length=150, blank=False, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, blank=False, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product/%Y/%m/%d')

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(blank=False)

    def __str__(self):
        return self.body