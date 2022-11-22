from django.db import models
from category.models import Category
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager
from datetime import timedelta,datetime

def default_start_time():
    start= datetime.now()+timedelta(hours=48)
    # start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start 

# Create your models here.
class MyProductManager(BaseUserManager):
    def create_product(self,product_name,description,price,images):

        product = self.model(
            product_name=product_name,
            description=description,
            images=images,
            price=price,
            
        
        )

        product.save(using=self._db)
        return product

    # def save(self,price):

    #     product = self.model(

    #         price=price,
            
    #     )

    #     product.save(using=self._db)
    #     return product

class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug =models.SlugField(max_length=200)
    description=models.TextField(blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'photos/products')
    stock=models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)
    # category=models.ForeignKtegorory_id=models.TextField(null=True)
    category=models.TextField(default="shoes",null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(default=default_start_time)
    current_winner=models.CharField(max_length=200)
    Bid_owner=models.CharField(max_length=200)
    objects=MyProductManager()

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail',args=[self.slug])


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(Variation_category='color',is_active=True)

    def size(self):
        return super(VariationManager,self).filter(Variation_category='size',is_active=True)

Variation_category_choice=(
    ('color','color'),
    ('size','size')
)

class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Variation_category = models.CharField(max_length=100,choices=Variation_category_choice)
    Variation_value =models.CharField(max_length=100)
    is_active  = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects=VariationManager()

    def __str__(self):
        return self.Variation_value

    
    
 