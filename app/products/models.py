from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)


class Product(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    # )
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    categories = models.ManyToManyField(Category)


class Order(models.Model):
    ordered_at = models.DateTimeField()
    customer_name = models.CharField(max_length=255)


class OrderItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
