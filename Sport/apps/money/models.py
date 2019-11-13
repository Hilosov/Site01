from django.db import models

# Create your models here.

class Infomation(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField('Текст')

    def __str__(self):
        return self.name

'''class Product(models.Model):
    title = models.TextField('Название чисто для теста')
    praice = models.DecimalField(max_digits=9, decimal_places=2)
    slug = models.SlugField()

class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for product {0}".format(self.product.title)

class Cart(models.Model):
    items = models.ForeignKey('CartItem', on_delete=models.CASCADE)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self(Id))'''

