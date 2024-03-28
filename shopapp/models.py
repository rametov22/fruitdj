from django.db import models
from django.core.validators import MinValueValidator
from homeapp.models import ProductModel
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ShopModel(models.Model):
    name = models.CharField('заголовок', max_length=255)
    content = models.TextField('content')
    price = models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=2, max_digits=6)
    img = models.ImageField('img', upload_to='shop/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    popularity = models.IntegerField(default=0)
    organic = models.BooleanField(default=False)
    fantastic = models.BooleanField(default=False)
    Organic = models.BooleanField(default=False)
    Fresh = models.BooleanField(default=False)
    Sales = models.BooleanField(default=False)
    Discount = models.BooleanField(default=False)
    Expired = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AddCart(models.Model):
    product_shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, null=True, blank=True)
    product_home = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        product_name = ''
        if self.product_home:
            product_name = self.product_home.name
        elif self.product_shop:
            product_name = self.product_shop.name
        return f'{self.quantity} x {product_name}'


class ShippingMethod(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField('text', null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    order_notes = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    cart_items = models.ManyToManyField(AddCart)

    def __str__(self):
        return f"Order for {self.user.username}"


class FeaturedModel(models.Model):
    name = models.CharField('name', max_length=255)
    img = models.ImageField('img', upload_to='shop/')
    first_price = models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=2, max_digits=6)
    disc_price = models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=2, max_digits=6)
    STAR_CHOICES = [
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ]
    stars = models.IntegerField(choices=STAR_CHOICES, default=4)

    def __str__(self):
        return self.name


class ShopBanner(models.Model):
    title = models.CharField('title1', max_length=255)
    title2 = models.CharField('title2', max_length=255)
    title3 = models.CharField('title3', max_length=255)
    img = models.ImageField('img', upload_to='shop/')

    def __str__(self):
        return self.title
