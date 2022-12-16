from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name = 'customer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    
    # the following is a static method because sinc
    @staticmethod
    def get_create_url():
        return reverse('main:customer-create',kwargs={} )

    @staticmethod
    def get_update_url():
        return reverse('main:customer-update',kwargs={} )

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.email}'


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f' {self.user.email}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(default=0)
    inventory = models.IntegerField()
    in_a_cart = models.BooleanField(default = False)
    amount_in_carts = models.IntegerField (default = 0)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    alt_image = models.ImageField(upload_to='product_images', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}, {self.category}'
    
    def exists_as_user_cartitem(self):
        if User.cart.items.get(product = self):
            return True
        return False

    def get_user_cartitem(self):
        return User.cart.items.get(product = self)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name = 'cartitems')
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'items')
    amount = models.IntegerField(default=1)

    cost = lambda self:self.amount*self.product.price
    
    def __str__(self):
        return f'{self.cart.user.email}, {self.product.name}, {self.amount}'
