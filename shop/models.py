from email.policy import default
from django.db import models
from django.forms import ImageField

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    pub_data = models.DateField()
    image = models.ImageField(upload_to = "shop/images", default="")
    
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    query = models.CharField(max_length=500, default='')
    
    def __str__(self):
        return self.name