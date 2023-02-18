from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.shortcuts import redirect
from django.utils.translation import gettext as _


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    image = models.ImageField(_('Avatar'), upload_to='user_images', null=True)
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'secretary'),
      (4, 'supervisor'),
      (5, 'admin'),
    )

    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, null=True)


    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    interests = models.ManyToManyField(Category, related_name='interested_users')

    def __str__(self):
        return self.full_name

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.full_name


class Product(models.Model):
    seller = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=2, decimal_places=2)
    inventory = models.IntegerField()
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name





'''

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name = 'customer')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=11)
#     email = models.EmailField()

    
#     # the following is a static method because sinc
#     @staticmethod
#     def get_create_url():
#         return reverse('main:customer-create',kwargs={} )

#     @staticmethod
#     def get_update_url():
#         return reverse('main:customer-update',kwargs={} )

#     @staticmethod
#     def get_customer_by_email(email):
#         try:
#             return Customer.objects.get(email=email)
#         except:
#             return False

#     def isExists(self):
#         if Customer.objects.filter(email=self.email):
#             return True
#         return False
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}, {self.email}'


# class Category(models.Model):
#     name = models.CharField(max_length=50)
    
#     def __str__(self) -> str:
#         return self.name


# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

#     def __str__(self):
#         return f' {self.user.email}'


# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     price = models.IntegerField(default=0)
#     inventory = models.IntegerField()
#     in_a_cart = models.BooleanField(default = False)
#     amount_in_carts = models.IntegerField (default = 0)
#     description = models.TextField()
#     image = models.ImageField(upload_to='product_images')
#     alt_image = models.ImageField(upload_to='product_images', blank=True, null=True)
    
#     def __str__(self):
#         return f'{self.name}, {self.category}'
    
#     def exists_as_user_cartitem(self):
#         if User.cart.items.get(product = self):
#             return True
#         return False

#     def get_user_cartitem(self):
#         return User.cart.items.get(product = self)


# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name = 'cartitems')
#     cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'items')
#     amount = models.IntegerField(default=1)

#     cost = lambda self:self.amount*self.product.price
    
#     def __str__(self):
#         return f'{self.cart.user.email}, {self.product.name}, {self.amount}'
'''