from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=1)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    condition = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField()

    def __str__(self):
        return self.name
