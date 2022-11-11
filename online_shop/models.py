from django.db import models


class Category (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null='Категория')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




